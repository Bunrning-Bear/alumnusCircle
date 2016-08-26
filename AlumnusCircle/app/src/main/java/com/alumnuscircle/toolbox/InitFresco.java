/**
 * @author zhengfanw
 * @date 16.08.26
 * 封装Fresco的初始化过程。
 */

package com.alumnuscircle.toolbox;

import android.content.Context;

import com.facebook.drawee.backends.pipeline.Fresco;


public class InitFresco {
    public InitFresco(Context context){
        Fresco.initialize(context);
    }

}
