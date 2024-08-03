/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package app.java.appdemocrud;

import java.sql.SQLException;

/**
 *
 * @author user
 */
public class AppDemoCrud {

    public static void main(String[] args) throws SQLException {
        MySQLConnection con = new MySQLConnection();
        con.DemoConector();
        
    }
}
