package com.yang.video.ddrk;

import cn.hutool.core.io.FileUtil;
import cn.hutool.core.io.StreamProgress;
import cn.hutool.http.HttpResponse;
import cn.hutool.http.HttpUtil;
import cn.hutool.json.JSONArray;
import cn.hutool.json.JSONObject;
import cn.hutool.json.JSONUtil;
import org.jsoup.Jsoup;
import org.jsoup.helper.StringUtil;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import java.io.*;
import java.util.*;

/**
 * desc
 *
 * @author woshilll
 * @version 1.0.0
 * @date 2021/9/17 15:55
 */
public class DdrkParse {
    public static final String SERVER1 = "https://v3.ddrk.me";
    public static final String SERVER2 = "https://v2.ddrk.me";
    public static final String SERVER_TV = "https://v.ddys.tv";
    public static void main(String[] args) throws Exception {
        download();
    }
    public static void download() throws Exception {
        HttpResponse execute = HttpUtil.createGet("https://ddrk.me/free-guy/").execute();
        String body = execute.body();
        Document document = Jsoup.parse(body);
        Element element = document.body();
        Element aClass = element.getElementsByClass("wp-playlist wp-video-playlist wp-playlist-light wpse-playlist").get(0);
        Element script = aClass.getElementsByTag("script").get(0);
        String json = script.html();
        JSONObject jsonObject = JSONUtil.parseObj(json);
        Object tracks = jsonObject.get("tracks");
        JSONArray jsonArray = JSONUtil.parseArray(tracks);
        List<Integer> skip = Arrays.asList(-1, -3);
        int i = 0;
        for (Object o : jsonArray) {
            i++;
            if (skip.contains(i)) {
                continue;
            }
            Object videoId = JSONUtil.parseObj(o).get("src0");
            System.out.println(videoId);
            String encryptStr = DdrkEncrypt.toStr((String) videoId, new Date());
            String downloadUrl =  tryServer(encryptStr);
            int lastIndexOf = ((String) videoId).lastIndexOf('_');
            String fileName = ((String) videoId).substring(lastIndexOf + 1);
            if (StringUtil.isBlank(downloadUrl)) {
                System.err.println(fileName + " --- 下载失败");
                return;
            }
            download(downloadUrl, fileName);
            Thread.sleep(60000);
        }
    }

    private static String tryServer(String encryptStr) throws InterruptedException {

        String request = ":9543/video?id=" + encryptStr + "&type=mix";
        System.out.println("尝试服务1 " + SERVER1 + request);
        String resJson = HttpUtil.createGet(SERVER1 + request)
                .execute().body();
        System.out.println("接收到服务器1的消息: " + resJson);
        Object downloadUrl = JSONUtil.parseObj(resJson).get("url");
        if (StringUtil.isBlank((String) downloadUrl)) {
            // server2
            Thread.sleep(1000);
            System.out.println("尝试服务2 " + SERVER2 + request);
            resJson = HttpUtil.createGet(SERVER2 + request)
                    .execute().body();
            System.out.println("接收到服务器2的消息: " + resJson);
            downloadUrl = JSONUtil.parseObj(resJson).get("url");
            if (StringUtil.isBlank((String) downloadUrl)) {
                // server2
                Thread.sleep(1000);
                System.out.println("尝试服务3 " + SERVER_TV + request);
                resJson = HttpUtil.createGet(SERVER_TV + request)
                        .execute().body();
                System.out.println("接收到服务器3的消息: " + resJson);
                downloadUrl = JSONUtil.parseObj(resJson).get("url");
            }
        }
        return (String) downloadUrl;
    }

    public static void download(String url, String fileName) {
        HttpUtil.downloadFile(url, new File("./rick/" + fileName), new StreamProgress() {
            @Override
            public void start() {
                System.out.println("开始下载 --- " + fileName);
            }

            @Override
            public void progress(long l) {
                if (l % 1000 == 0) {
                    System.out.println("已下载：" + FileUtil.readableFileSize(l));
                }
            }

            @Override
            public void finish() {
                System.out.println("下载完成");
            }
        });
    }
}
