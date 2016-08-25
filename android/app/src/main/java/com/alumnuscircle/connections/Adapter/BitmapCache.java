package com.alumnuscircle.connections.Adapter;

import android.graphics.Bitmap;
import android.util.LruCache;

import com.android.volley.toolbox.ImageLoader;

/**
 * Created by 曾博晖 on 2016/7/29.
 * 继承自ImageCache，实现对加载后网络图片的本地存储
 */
public class BitmapCache implements ImageLoader.ImageCache {

    private LruCache<String, Bitmap> mCache;

    public BitmapCache() {
        int maxSize = 10 * 1024 * 1024;
        mCache = new LruCache<String, Bitmap>(maxSize) {
            @Override
            protected int sizeOf(String key, Bitmap bitmap) {
                return bitmap.getRowBytes() * bitmap.getHeight();
            }
        };
    }

    @Override
    public Bitmap getBitmap(String url) {
        return mCache.get(url);
    }

    @Override
    public void putBitmap(String url, Bitmap bitmap) {
        mCache.put(url, bitmap);
    }

}