/**
 * @author zhengfanw
 * @version 1
 * @date 16.08.18
 * 功能：这个类继承了Application，并且在AndroidManifest.xml中声明为程序的真正入口，
 * 并且覆盖整个程序的生命周期，可以方便后期进行一些工具对象的初始化。
 * Note:这个App用到的第三方开源库有：Gson、Okhttp、Fresco、Volley
 */

package com.alumnuscircle;

import android.app.Application;

import com.alumnuscircle.toolbox.InitFresco;

public class CircleApplication extends Application {

    @Override
    public void onCreate() {
        super.onCreate();
        initFresco();
    }

    /**
     * 初始化，顺序有要求。
     */
    private void init(){
        initFresco();
    }

    /**
     * 初始化Fresco
     */
    private void initFresco(){
        new InitFresco(getApplicationContext());
    }
}
