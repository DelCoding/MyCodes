import java.net.*;
import java.io.*;
import java.util.Scanner;

public class MulitClient {
    public static void main(String[] args) throws IOException{
        // 在getByName()中，使用null作为参数
        // 来指定本地服务器的地址
        InetAddress addr = InetAddress.getByName(null);
        Scanner sc = new Scanner(System.in);
        System.out.print("即将进入聊天室，请输入你的别名：");
        String name = sc.nextLine();
        System.out.println("你的地址是：" + addr);
        Socket socket = new Socket(addr, 8080);

        // 为每个socket创建读进程，因为需要一直监听信息
        new ReadThread(socket).start();
        // 为每个socket创建写进程
        new WriteThread(socket, name).start();

    }
}

class ReadThread extends Thread{
    Socket socket;

    public ReadThread(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {

        try {
            BufferedReader in = new BufferedReader(new InputStreamReader
                    (this.socket.getInputStream()));

            while (true) {
                String str = in.readLine();
                System.out.println(str);
            }
        } catch (IOException e) {
            System.out.println("Socket读写错误！" + e.getStackTrace());
        }

    }
}

class WriteThread extends Thread{
    Socket socket;
    String name;
    public WriteThread(Socket socket, String name) {
        this.socket = socket;
        this.name = name;
    }

    @Override
    public void run(){
        Scanner sc = new Scanner(System.in);
        try {
            PrintWriter out =new PrintWriter(new BufferedWriter(new OutputStreamWriter
                    (socket.getOutputStream())),true);

            while (true) {
                System.out.println(">>");
                String str = sc.nextLine();
                str = this.name + "说：" +str;
                str = str.trim();
                if (str == "exit") {
                    break;
                }

                out.println(str);
            }
        } catch (IOException e){
            System.out.println("Socket读写错误！" + e.getStackTrace());
        }
    }
}
