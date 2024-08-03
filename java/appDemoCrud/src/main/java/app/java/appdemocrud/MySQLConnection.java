
package app.java.appdemocrud;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class MySQLConnection {
    private Connection connection = null;
    private Statement statement = null;
    private ResultSet resultset = null;
    
    public void DemoConector() throws SQLException{
        
        String url = "jdbc:mysql://localhost/demo_db?user=root&password=1239875";
        String sql = "select * from usuario";
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            connection = DriverManager.getConnection(url);
            
            
            statement = connection.createStatement();
            resultset = statement.executeQuery(sql);
            
            while(resultset.next()){
                System.out.println(resultset.getInt("id"));
                System.out.println(resultset.getString("name"));
                System.out.println(resultset.getString("email"));
            }
        }catch(ClassNotFoundException | SQLException e){
            System.err.println(e.getMessage());
        }finally{
            if(resultset != null) {resultset.close(); resultset = null;}
            if(statement != null) {statement.close(); statement = null;}
            if(connection != null) {connection.close(); connection = null;}
        }
    }
    public void SQLServer(){
        String url = "jdbc:sqlserver://JORD;databaseName=dimo";
        
        // Nombre de usuario y contraseña de la base de datos
        String usuario = "sa";
        String contraseña = "1239875";
        
        // Intentar establecer la conexión
        try {
            Connection conexion = DriverManager.getConnection(url, usuario, contraseña);
            //return conexion();
            System.out.println("Conexión exitosa a SQL Server");
            // Aquí puedes realizar operaciones con la base de datos
            // Por ejemplo, ejecutar consultas SQL o actualizar datos
            // Recuerda cerrar la conexión cuando hayas terminado de usarla
            conexion.close();
        } catch (SQLException e) {
            System.out.println("XXXXXXX: " + e.getMessage());
        }
    }
}
/**/