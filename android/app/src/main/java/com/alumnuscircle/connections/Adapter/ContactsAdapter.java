package com.alumnuscircle.connections.Adapter;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;


import com.alumnuscircle.connections.Adapter.BitmapCache;
import com.alumnuscircle.connections.Image.CircleNetworkImage;
import com.alumnuscircle.connections.Item.ContactsItem;
import com.android.volley.RequestQueue;
import com.android.volley.toolbox.ImageLoader;
import com.android.volley.toolbox.NetworkImageView;
import com.android.volley.toolbox.Volley;
import com.alumnuscircle.R;

import java.util.List;

/**
 * Created by 曾博晖 on 2016/8/10.
 * 实现Contacts的RecycleView适配器
 */

public class ContactsAdapter extends RecyclerView.Adapter<ContactsAdapter.MyViewHolder> {
    private List<ContactsItem> contactsItemList;
    private Context mContext;
    private LayoutInflater inflater;
    private OnItemClickListener mOnItemClickListener;


    public ContactsAdapter(Context context,List<ContactsItem> contactsItems){
        this.mContext=context;
        this.contactsItemList=contactsItems;
        inflater=LayoutInflater.from(mContext);
    }


    @Override
    public MyViewHolder onCreateViewHolder( ViewGroup parent, int viewType) {
        View view=inflater.inflate(R.layout.item_contacts,parent,false);
        MyViewHolder holder=new MyViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(MyViewHolder holder, final int position) {
        holder.name_text.setText(contactsItemList.get(position).getUserName());
        holder.addr_text.setText(contactsItemList.get(position).getUserLocation());
        holder.grade_text.setText(contactsItemList.get(position).getUserGrade());
        holder.class_text.setText(contactsItemList.get(position).getUserClass());
        holder.job_text.setText(contactsItemList.get(position).getUserJob());
        Load_HeadPortrait(holder.head_img,
                contactsItemList.get(position).getHeadImgUrl());
        if( mOnItemClickListener!= null){
            holder. itemView.setOnClickListener( new View.OnClickListener() {

                @Override
                public void onClick(View v) {
                    mOnItemClickListener.onClick(position);
                }
            });

            holder. itemView.setOnLongClickListener( new View.OnLongClickListener() {
                @Override
                public boolean onLongClick(View v) {
                    mOnItemClickListener.onLongClick(position);
                    return false;
                }
            });
        }

    }

    @Override
    public int getItemCount() {
        return contactsItemList.size();
    }

//    /**
//     * 实现添加数据的操作
//     * 曾博晖
//     * 2016年8月10日18:07:37
//     * 添加注释
//     * */
//    public void addData(int position)
//    {
//        contactsItemList.add(position, new ContactsItem("http://v1.qzone.cc/avatar/201412/06/14/03/54829c3a87cd3532.jpg%21200x200.jpg",
//                "盼盼"));
//        notifyItemInserted(position);
//    }
    /**
     * 实现移除数据的操作
     * 曾博晖
     * 2016年8月10日18:08:17
     * 添加注释
     * */
    public void removeData(int position)
    {
        contactsItemList.remove(position);
        notifyItemRemoved(position);
    }


    public class MyViewHolder extends RecyclerView.ViewHolder{
        CircleNetworkImage head_img;
        TextView name_text;
        TextView grade_text;
        TextView class_text;
        TextView addr_text;
        TextView job_text;

        public MyViewHolder(View itemView) {
            super(itemView);
            head_img=(CircleNetworkImage) itemView.findViewById(R.id.headImg);
            name_text=(TextView)itemView.findViewById(R.id.userName_textView);
            grade_text=(TextView)itemView.findViewById(R.id.grade_textView);
            class_text=(TextView)itemView.findViewById(R.id.class_textView);
            addr_text=(TextView)itemView.findViewById(R.id.addr_textView);
            job_text=(TextView)itemView.findViewById(R.id.job_textView);
        }
    }
    /**
     * 利用Volley的Http请求进行加载头像的操作
     * 曾博晖
     * 2016年8月6日 创建
     * */
    public void Load_HeadPortrait(NetworkImageView networkImageView,String img_url) {
        RequestQueue mQueue = Volley.newRequestQueue(mContext);//申请一个队列
        ImageLoader imageLoader = new ImageLoader(mQueue, new BitmapCache() {
        });
        networkImageView.setErrorImageResId(R.mipmap.ic_launcher);
        networkImageView.setImageUrl(img_url,imageLoader);
    }

    /**
     * 定义条目点击接口，实现RecycleView的点击事件
     * 实现点击事件和长按事件
     * 曾博晖 2016年8月10日17:11:20 创建
     * */
    public interface OnItemClickListener{
        void onClick( int position);
        void onLongClick( int position);
    }
    /**
     * 设置点击事件的监听器
     * 曾博晖
     * 2016年8月10日17:14:05 创建
     * */
    public void setOnItemClickListener(OnItemClickListener onItemClickListener ){
        this. mOnItemClickListener=onItemClickListener;
    }
}
