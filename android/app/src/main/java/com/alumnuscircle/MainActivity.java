package com.alumnuscircle;


import android.app.FragmentTransaction;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import android.view.View;

import android.widget.Button;
import android.widget.ImageView;


import com.alumnuscircle.fragment.ContactsFragment;
import com.alumnuscircle.fragment.FindCirFragment;
import com.alumnuscircle.fragment.HomeFragment;
import com.alumnuscircle.fragment.MeFragment;
import com.alumnuscircle.fragment.MessageFragment;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {


    private ContactsFragment contactsFragment;
    private HomeFragment homeFragment;
    private FindCirFragment findCirFragment;
    private MeFragment meFragment;
    private MessageFragment messageFragment;
    private FragmentTransaction switchFragment;//更换fragment

    private ImageView home;
    private ImageView contacts;
    private ImageView findCir;
    private ImageView msg;
    private ImageView me;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        InitView();
        Button button =(Button)findViewById(R.id.test);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                startActivity(new Intent("com.alumnuscircle.circleDetail.CircleDetail"));
            }
        });



    }

    /**
     * 初始化界面
     */
    private  void InitView()
    {
        //初始化按钮
        home = (ImageView) findViewById(R.id.homepage);
        contacts = (ImageView)findViewById(R.id.contacts);
        findCir =(ImageView)findViewById(R.id.findcircle);
        msg = (ImageView)findViewById(R.id.message);
        me = (ImageView)findViewById(R.id.me);

        home.setBackgroundResource(R.mipmap.homepage_pressed);
        contacts.setBackgroundResource(R.mipmap.contacts);
        findCir.setBackgroundResource(R.mipmap.findcircle);
        me.setBackgroundResource(R.mipmap.me);
        msg.setBackgroundResource(R.mipmap.message);

        //初始化fragment
        switchFragment = getFragmentManager().beginTransaction();

        homeFragment = new HomeFragment();
        findCirFragment = new FindCirFragment();
        meFragment = new MeFragment();
        contactsFragment = new ContactsFragment();
        messageFragment = new MessageFragment();

        switchFragment.add(R.id.fragment,findCirFragment).hide(findCirFragment);
        switchFragment.add(R.id.fragment,meFragment).hide(meFragment);
        switchFragment.add(R.id.fragment,contactsFragment).hide(contactsFragment);
        switchFragment.add(R.id.fragment,messageFragment).hide(messageFragment);
        switchFragment.add(R.id.fragment,homeFragment);
        switchFragment.commit();

        //设置监听
        me.setOnClickListener(this);
        home.setOnClickListener(this);
        contacts.setOnClickListener(this);
        msg.setOnClickListener(this);
        findCir.setOnClickListener(this);
    }




    /**
     * 初始化监听的fragment
     */
    private void InitFragment()
    {
        //重新加载fragment选择器
        switchFragment = getFragmentManager().beginTransaction();
        //隐藏所有fragment
        if(homeFragment!=null)
            switchFragment.hide(homeFragment);
        if(findCirFragment!=null)
            switchFragment.hide(findCirFragment);
        if(meFragment!=null)
            switchFragment.hide(meFragment);
        if(messageFragment!=null)
            switchFragment.hide(messageFragment);
        if(contactsFragment!=null)
            switchFragment.hide(contactsFragment);

        //初始化所有图标
        home.setBackgroundResource(R.mipmap.homepage);
        contacts.setBackgroundResource(R.mipmap.contacts);
        findCir.setBackgroundResource(R.mipmap.findcircle);
        msg.setBackgroundResource(R.mipmap.message);
        me.setBackgroundResource(R.mipmap.me);
    }

    @Override
    public void onClick(View v) {

        InitFragment();

        switch (v.getId())
        {
            case R.id.homepage:
                if(homeFragment==null)
                {
                    homeFragment = new HomeFragment();
                  switchFragment.add(R.id.fragment,homeFragment);

                }
                else{
                    switchFragment.show(homeFragment);
                }

                home.setBackgroundResource(R.mipmap.homepage_pressed);
                break;
            case R.id.contacts:
                if(contactsFragment==null)
                {
                    contactsFragment = new ContactsFragment();
                    switchFragment.add(R.id.fragment,contactsFragment);
                }
                else{
                    switchFragment.show(contactsFragment);
                }

                contacts.setBackgroundResource(R.mipmap.contacts_pressed);
                break;
            case R.id.findcircle:
                if(findCirFragment==null)
                {
                    findCirFragment = new FindCirFragment();
                    switchFragment.add(R.id.fragment,findCirFragment);
                }
                else
                {
                    switchFragment.show(findCirFragment);
                }

                findCir.setBackgroundResource(R.mipmap.findcircle_pressed);
                break;
            case R.id.me:
                if(meFragment == null)
                {
                    meFragment = new MeFragment();
                    switchFragment.add(R.id.fragment,meFragment);
                }
                else
                {
                    switchFragment.show(meFragment);
                }

                me.setBackgroundResource(R.mipmap.me_pressed);
                break;
            case R.id.message:


            if(messageFragment == null)
                {
                    messageFragment = new MessageFragment();
                    switchFragment.add(R.id.fragment,messageFragment);
                }
                else {
                    switchFragment.show(messageFragment);
                }
            msg.setBackgroundResource(R.mipmap.message_pressed);
            break;
        }
        switchFragment.commit();
    }

    @Override
    protected void onSaveInstanceState(Bundle outState) {
//        super.onSaveInstanceState(outState);
        //阻止保存状态解决fragment重叠
    }
}
