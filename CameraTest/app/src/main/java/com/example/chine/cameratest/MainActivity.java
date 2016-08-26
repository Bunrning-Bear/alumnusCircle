package com.example.chine.cameratest;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Environment;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.File;
import java.io.IOException;

public class MainActivity extends Activity {

    private Button cameraBtn;
    private Button galleryBtn;
    private File imageFile;
    private Uri tmpuri;
    private Bitmap bitmap;
    private ImageView img;

    private static final String TEMP_TAKE_PHOTO_FILE_PATH = Environment.getExternalStorageDirectory() + File.separator
            + "alumnusCircle" + File.separator + "myAlbum" + File.separator;
    private static final int TAKE_PHOTO_REQUEST_CODE = 0x10086;
    private static final int SELECT_PHOTO_REQUEST_CODE = 0x10087;
    private static final int CUT_PHOTO_REQUEST_CODE = 0x10088;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
    }

    private void init(){
        initBtn();
        img = (ImageView)findViewById(R.id.img);
    }

    private void initBtn(){
        cameraBtn = (Button)findViewById(R.id.camera_btn);
        galleryBtn = (Button)findViewById(R.id.gallery_btn);

        cameraBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gotoCamera();
            }
        });

        galleryBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                gotoGallery();
            }
        });
    }

    private void gotoCamera(){
        Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        File imageDir = new File(TEMP_TAKE_PHOTO_FILE_PATH);
        if (!imageDir.exists())
        {
            imageDir.mkdirs();
        }
        try {
            imageFile = File.createTempFile(""+System.currentTimeMillis(), ".jpg", imageDir);
            tmpuri = Uri.fromFile(imageFile);
            intent.putExtra(MediaStore.EXTRA_OUTPUT, tmpuri);
            startActivityForResult(intent, TAKE_PHOTO_REQUEST_CODE);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private void gotoGallery(){
        Intent innerIntent = new Intent(Intent.ACTION_GET_CONTENT);
        innerIntent.setType("image/*");
        Intent wrapperIntent = Intent.createChooser(innerIntent, null);
        startActivityForResult(wrapperIntent, SELECT_PHOTO_REQUEST_CODE);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (requestCode == TAKE_PHOTO_REQUEST_CODE || requestCode == SELECT_PHOTO_REQUEST_CODE) {

            if (resultCode == RESULT_OK) {
                Uri uri = null;
                if (requestCode == SELECT_PHOTO_REQUEST_CODE) {
                    uri = data.getData();
                } else if (requestCode == TAKE_PHOTO_REQUEST_CODE) {
                    uri = tmpuri;
                }
                if (uri != null) {
                    final Intent intent = new Intent("com.android.camera.action.CROP");
                    intent.setDataAndType(uri, "image/*");
                    intent.putExtra("crop", "true");
                    intent.putExtra("aspectX", 1);
                    intent.putExtra("aspectY", 1);
                    intent.putExtra("outputX", 400);
                    intent.putExtra("outputY", 400);
                    intent.putExtra("scale", true);
                    intent.putExtra("return-data", true);
                    intent.putExtra("outputFormat", Bitmap.CompressFormat.JPEG.toString());
                    startActivityForResult(intent, CUT_PHOTO_REQUEST_CODE);
                }
            }
        } else if (requestCode == CUT_PHOTO_REQUEST_CODE) {
            if (resultCode == RESULT_OK && data != null) {
                bitmap = data.getParcelableExtra("data");
                img.setImageBitmap(bitmap);
            }
        }
    }
}
