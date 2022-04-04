package com.yang.video.ddrk;

import javax.crypto.Cipher;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import java.security.Security;
import java.util.Base64;
import java.util.Date;

/**
 * desc
 *
 * @author woshilll
 * @version 1.0.0
 * @date 2021/9/17 15:52
 */
public class DdrkEncrypt {
    private static final String ENCRYPT_TYPE = "AES/CBC/PKCS7Padding";
    private static final String ENCRYPT_KEY = "zevS%th@*8YWUm%K";
    private static final String IV = "5080305495198718";
    private static Cipher cipher;
    static {
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        try {
            cipher = Cipher.getInstance(ENCRYPT_TYPE);
        } catch (NoSuchAlgorithmException | NoSuchPaddingException e) {
            e.printStackTrace();
        }
    }

    /**
     * /v/Anime/rick_and_morty/rick_morty_s05e01.mp4
     */
    public static String toStr(String videoId, Date resDate) throws Exception {

        cipher.init(Cipher.ENCRYPT_MODE, new SecretKeySpec(ENCRYPT_KEY.getBytes(), "AES"), new IvParameterSpec(IV.getBytes()));
        String content = "{\"path\":\"" + videoId + "\",\"expire\":" + (resDate.getTime() + 600000) + "}";
        byte[] encryptStr = cipher.doFinal(content.getBytes(StandardCharsets.UTF_8));
        return URLEncoder.encode(Base64.getEncoder().encodeToString(encryptStr), "utf-8");
    }
}
