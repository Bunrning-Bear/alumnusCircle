- ## 统一规范：
	- 的返回形式是json，包括三个大的字段：
        - code：返回的代码，可能是错误代码，可能是正确代码
        - message：这个代码对应的信息，仅用于便于客户端理解
        - Data: 这个是一个可选的参数，如果没有这个参数，那么客户端会收到‘{}’，否则，是一个json数组
	- 使用的中文编码是 json 默认的 unicode编码，比如：
    	\"name\": \"\\u9648\\u96c4\\u8f89\"
    - 返回值都有code,message.下面所讲的返回值指的是：Data部分[如果有的话]。
    - 项目的错误代码我是写了一个生成函数，每个代码对应一个错误消息，但是哪个错误对应哪个消息，没有进行统计，之后再看把。
	- POST 的 header： ”Content-Type: application/x-www-form-urlencoded“

## register, login and logout.
- #### 获取客户端令牌：
	- api:/
	- http method: get
	- request:
		none
    - response:
    	- "{\"_xsrf\": \"49608c3c790244a19fe996530d631d32\"}"
    	- _xsrf 是用户本次回话所需要的表单，以后每次访问都需要使用post请求携带这个_xsrf参数，来保证客户端身份的合法性，下不赘述。

- #### 注册:
	- api:/register
	- http method: post
	- request:
		- _xsrf
        - info_json:
"city": 三位数城市代号，具体根据之后得到的城市列表信息而做调整
"faculty_id": 1-2位数的院系代号
"name": "陈雄辉", 姓名，2~20位数，可以是中文
"major_id": 1,专业代号，1~2位数
"company": "the SEU",公司名字，可以中文英文，空格，2~25
"admission_year": 2014, 入学年份，4位整形
"telephone": 15105861442,手机号
"job": "student",工作，可中文，2~20位的中文或者英文，可以空格
"gender": 1,性别 0 女，1 男
"password": "XXXXX" 密码，客户端需要进行md5加密
	- response:
        - code
        - message.
    - example:
		- request:
			- _xsrf:49608c3c790244a19fe996530d631d32
			- info_json:
            {
                "city": 123,
                "faculty_id": 71,
                "name": "陈雄辉",
                "major_id": 1,
                "company": "the SEU",
                "admission_year": 2014,
                "telephone": 15105861442,
                "job": "student",
                "gender": 1,
                "password": "XXXX"，
                “icon_url”:“default” 用户需要上传的图片的URL，图片上传还没实现，暂时不出理
            }
		- response:
			{"message": "login successfully!", "code": 2700, "Data": "{}"}
- #### 登录：[此时暂时不考虑缓存和自动登录，如果考虑之后，这部分的逻辑需要重新写。]
	- api:/login
	- http method: post
	- request:
		- _xsrf
        - info_json:{
            "password": "XXXXX" 密码，客户端需要进行md5加密,
            "telephone": 15105861442,手机号
        }
	- response:
		- code
		- message
		- Data:
			"city"
    		"faculty_id"
            "major_id":
    		"gender"
    		"uid",用于标志用户身份的uid
    		"tags"，标签，暂时不使用
    		"icon_url"， 图片的url，目前统一返回：\"default\",
    		"company"，
    		"admission_year"，
    		"my_circle_list"：我加入的圈子列表，这里面是另一个json数组
    		"job_list_level": 0, 该用户对于自己的工作身份的开放程度，0表示对所有人开放。
    		"job": "student",
    		"protect_contact_list"：记录用户的私人的联系方式，只能对圈内的人开放，
    		"detail_id":用户在mysql里面的id，客户端不需要处理
    		"company_publicity_level": 0,该用户对于自己的所在公司的开放程度，0表示对所有人开放。
    		"public_contact_list"： 用户设置的公共电话，这里面是一个json，对圈外人开放
			"instroduction\":用户的自我介绍，是一个最大长度位350个字符的字符串。
    		"job_list":工作经历列表，是一个json
    		"name":
}
	- example：
        - request:
        	- _xsrf=49608c3c790244a19fe996530d631d32&
			- info_json={"password": "XXXX","telephone": "15105861442"}
		- response:
			{
    "message": "login successfully!",
    "code": 1202,
    "Data": "{\"city\": 123, \"faculty_id\": 71, \"gender\": 1, \"uid\": 1, \"tags\": \"{}\", \"icon_url\": \"default\", \"company\": \"the SEU\", \"admission_year\": 2014, \"my_circle_list\": \"{}\", \"job_list_level\": 0, \"job\": \"student\", \"protect_contact_list\": \"{}\", \"detail_id\": 1, \"company_publicity_level\": 0, \"public_contact_list\": \"{}\", \"major_id\": 1, \"instroduction\": \"{}\", \"job_list\": \"{}\", \"name\": \"\\u9648\\u96c4\\u8f89\"}"
}
- #### 注销：
	- api:/logout
	- http method: post
	- request:
		- _xsrf
	- reponse:
		- code,message.
	-example:
    	{"message": "logout successfully!", "code": 3, "Data": "{}"}