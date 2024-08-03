/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package app.java.sistemadenotas;

//import clases.IngresoDatos;
import clases.principal;
import javax.swing.JFrame;

/**
 *
 * @author user
 */
public class SistemaDeNotas {

    public static void main(String[] args) {
        //System.out.println("Hello World!");
        //IngresoDatos vPrincipal = new IngresoDatos();
        principal vPrincipal = new principal();
        vPrincipal.setTitle("Sistema de Ingreso de Notas");
        vPrincipal.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        vPrincipal.setExtendedState(vPrincipal.getExtendedState() | JFrame.MAXIMIZED_BOTH);
        vPrincipal.setVisible(true);
        //vPrincipal.show();
    }
}
