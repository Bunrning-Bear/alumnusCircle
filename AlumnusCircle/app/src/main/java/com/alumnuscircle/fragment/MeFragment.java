/**
 * @author 吴正凡
 * @date 16.08.26
 * 这是主页中，“我的”分页。
 */

package com.alumnuscircle.fragment;

import android.app.Fragment;
import android.app.FragmentManager;
import android.app.FragmentTransaction;
import android.net.Uri;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.alumnuscircle.R;
import com.alumnuscircle.myself.AdminCircle;
import com.alumnuscircle.myself.CollectCards;
import com.alumnuscircle.myself.JoinCircle;
import com.facebook.drawee.view.SimpleDraweeView;


public class MeFragment extends Fragment {

    private View view;
    private LayoutInflater layoutInflater;
    private ViewGroup container;

    private SimpleDraweeView userHeadImg;
    private RelativeLayout cameraBtn;
    private TextView userName;
    private TextView userCareer;
    private TextView userMajor;
    private ImageView settingBtn;
    private LinearLayout collectCardsBtn;
    private LinearLayout joinCircleBtn;
    private LinearLayout adminCircleBtn;
    private ImageView collectCardsLine;
    private ImageView joinCircleLine;
    private ImageView adminCircleLine;

    private FragmentManager fragmentManager;
    private FragmentTransaction fragmentTransaction;
    private Fragment currentFragment;
    private Fragment collectCards;
    private Fragment joinCircle;
    private Fragment adminCircle;


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.fragment_me, container, false);
        layoutInflater = inflater;
        this.container = container;
        init();
        return view;
    }

    private void init(){
        initUIBtn();
        initFragment();
        initCollectCards();
        initData();
    }

    private void initData(){
        userHeadImg.setImageURI(Uri.parse("http://cdn.duitang.com/uploads/item/201512/10/20151210154332_VCGvy.png"));
        userName.setText("马天宇");
        userCareer.setText("首席架构师");
        userMajor.setText("软件学院2014级 · 2班");
    }

    private void initUIBtn(){
        settingBtn = (ImageButton)view.findViewById(R.id.me_setting_btn);
        userHeadImg = (SimpleDraweeView)view.findViewById(R.id.me_headimg);
        cameraBtn = (RelativeLayout)view.findViewById(R.id.me_camera_btn);
        userName = (TextView)view.findViewById(R.id.me_user_name);
        userCareer = (TextView)view.findViewById(R.id.me_user_career);
        userMajor = (TextView)view.findViewById(R.id.me_user_major);
        collectCardsBtn = (LinearLayout)view.findViewById(R.id.me_collect_cards_btn);
        joinCircleBtn = (LinearLayout)view.findViewById(R.id.me_join_circle_btn);
        adminCircleBtn = (LinearLayout)view.findViewById(R.id.me_admin_circle_btn);
        collectCardsLine = (ImageView)view.findViewById(R.id.me_collect_cards_line);
        joinCircleLine = (ImageView)view.findViewById(R.id.me_join_circle_line);
        adminCircleLine = (ImageView)view.findViewById(R.id.me_admin_circle_line);

        settingBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        cameraBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        collectCardsBtn.setOnClickListener(new TabBtnClickListener());
        joinCircleBtn.setOnClickListener(new TabBtnClickListener());
        adminCircleBtn.setOnClickListener(new TabBtnClickListener());

    }

    private void initFragment(){
        fragmentManager = this.getFragmentManager();
        fragmentTransaction = fragmentManager.beginTransaction();
    }

    /**
     * 第一次进入主页页面，默认是显示CollectCards这个页面，
     * 也就是第一个页面，所以需要在进入本Fragment就初始一次。
     */
    private void initCollectCards() {
        if (collectCards == null) {
            collectCards = new CollectCards();
        }
        if (!(collectCards.isAdded())) {
            if (fragmentTransaction == null) {
                fragmentManager = this.getFragmentManager();
                fragmentTransaction = fragmentManager.beginTransaction();
            }
            fragmentTransaction.add(R.id.contentFragmentLayout, collectCards).commit();
        }
        currentFragment = collectCards;
        collectCardsBtn.setSelected(true);
        collectCardsBtn.setEnabled(false);
        collectCardsLine.setSelected(true);
        joinCircleBtn.setSelected(false);
        joinCircleBtn.setEnabled(true);
        joinCircleLine.setSelected(false);
        adminCircleBtn.setSelected(false);
        adminCircleBtn.setEnabled(true);
        adminCircleLine.setSelected(false);
    }

    /**
     * 点击导航栏中“收藏的名片”按钮之后的动作。
     */
    public void clickCollectCardsBtn() {
        if (collectCards == null) {
            collectCards = new CollectCards();
        }
        switchFragment(collectCards);
        collectCardsBtn.setSelected(true);
        collectCardsBtn.setEnabled(false);
        collectCardsLine.setSelected(true);
        joinCircleBtn.setSelected(false);
        joinCircleBtn.setEnabled(true);
        joinCircleLine.setSelected(false);
        adminCircleBtn.setSelected(false);
        adminCircleBtn.setEnabled(true);
        adminCircleLine.setSelected(false);
    }

    /**
     * 点击导航栏中“参与的圈子”按钮之后的动作。
     */
    public void clickJoinCircleBtn() {
        if (joinCircle == null) {
            joinCircle = new JoinCircle();
        }
        switchFragment(joinCircle);
        collectCardsBtn.setSelected(false);
        collectCardsBtn.setEnabled(true);
        collectCardsLine.setSelected(false);
        joinCircleBtn.setSelected(true);
        joinCircleBtn.setEnabled(false);
        joinCircleLine.setSelected(true);
        adminCircleBtn.setSelected(false);
        adminCircleBtn.setEnabled(true);
        adminCircleLine.setSelected(false);
    }

    /**
     * 点击导航栏中“管理的圈子”按钮之后的动作。
     */
    public void clickAdminCircleBtn() {
        if (adminCircle == null) {
            adminCircle = new AdminCircle();
        }
        switchFragment(adminCircle);
        collectCardsBtn.setSelected(false);
        collectCardsBtn.setEnabled(true);
        collectCardsLine.setSelected(false);
        joinCircleBtn.setSelected(false);
        joinCircleBtn.setEnabled(true);
        joinCircleLine.setSelected(false);
        adminCircleBtn.setSelected(true);
        adminCircleBtn.setEnabled(false);
        adminCircleLine.setSelected(true);
    }


    /**
     * 实现Fragment的切换。
     *
     * @param f 要切换去的fragment。
     */
    private void switchFragment(Fragment f) {
        fragmentManager = this.getFragmentManager();
        fragmentTransaction = fragmentManager.beginTransaction();
        if (f == currentFragment) {
            return;
        }
        if (f.isAdded()) {
            fragmentTransaction.hide(currentFragment).show(f).commit();
        } else {
            fragmentTransaction.hide(currentFragment).add(R.id.contentFragmentLayout, f).commit();
        }
        currentFragment = f;
    }

    /**
     * 导航栏按钮的监听类。
     */
    class TabBtnClickListener implements View.OnClickListener {
        @Override
        public void onClick(View v) {
            switch (v.getId()) {
                case R.id.me_collect_cards_btn:
                    clickCollectCardsBtn();
                    break;
                case R.id.me_join_circle_btn:
                    clickJoinCircleBtn();
                    break;
                case R.id.me_admin_circle_btn:
                    clickAdminCircleBtn();
                    break;
                default:
                    break;
            }
        }
    }

}
