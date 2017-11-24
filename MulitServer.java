import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class MulitServer {
    // 创建 Socket列表，存放客户端socket
    static ArrayList<Socket> clientList = new ArrayList<Socket>();
    public static void main(String[] args) throws IOException{
        ServerSocket server = new ServerSocket(8080);
        System.out.println("Started: " + server);
        while (true){
            Socket client = server.accept();
            clientList.add(client);

            String str = String.format("欢迎加入聊天室！当前人数为：%d", clientList.size());
            PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter
                    (client.getOutputStream())),true);

            out.println(str);
            // 为每个客户端socket创建一个线程，专门转发信息
            new ServerThread(client,clientList).start();
        }
    }
}

class ServerThread extends Thread{
    Socket self;
    ArrayList<Socket> list;

    public ServerThread(Socket self, ArrayList<Socket> list){
        this.self = self;
        this.list = list;
    }

    @Override
    public void run(){
        try {
            System.out.println("Connection accepted: "+ this.self);
            BufferedReader in = new BufferedReader(new InputStreamReader
                    (this.self.getInputStream()));

            while (true) {
                String str = "";
                str = in.readLine();
                System.out.println("Server received: " + this.self);
                System.out.println("Message is: " + str);

                for (int i = 0; i < this.list.size(); i++) {
                    // 不用给自己发送信息
                    if (this.list.get(i).getPort() == this.self.getPort()){
                        continue;
                    }
                    PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter
                            (this.list.get(i).getOutputStream())),true);
                    // 发送信息
                    out.println(str);
                }
            }
        } catch (IOException e){
            System.out.println("Socket读写错误！" + e.getStackTrace());
        }

    }
}
