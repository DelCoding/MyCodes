# 如何在idea下使用JavaBean
&emsp;首先在 src 文件夹下创建一个package，不能直接创建类，不然会导入失败。然后在这个包下创建Students类。
所以整个项目结构为：<br>
![image](https://github.com/DelCoding/MyCodes/blob/master/images/2.png)

&emsp;Students.java的内容如下：
```java
package test;

public class Students {
    private String name;
    private String email;
    private String phone;

    public String getEmail() {
        return email;
    }

    public String getName() {
        return name;
    }

    public String getPhone() {
        return phone;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
}
```

&emsp;在需要使用这个类的jsp文件里，导入这个bean。
&emsp;第一种方法如下：
```jsp
                <%-- 使用JavaBean，需要先在src下新建一个package，不能直接创建Students类，不然会导入失败。--%>
                <jsp:useBean id="students" class="test.Students">
                    <jsp:setProperty name="students" property="*" />
                </jsp:useBean>

  <h3>
              姓名：<%= students.getName() %><br>
              邮箱：<%= students.getEmail() %><br>
              电话：<%= students.getPhone() %><br>
  </h3>
  ```
  &emsp;第二种方式：
  ```jsp
                  <%@page import="test.Students" %>
                <% Students students = new Students();
                    students.setName(name);
                    students.setEmail(email);
                    students.setPhone(phone);
                %>
  <h3>
              姓名：<%= students.getName() %><br>
              邮箱：<%= students.getEmail() %><br>
              电话：<%= students.getPhone() %><br>
  </h3>
  ```
  
