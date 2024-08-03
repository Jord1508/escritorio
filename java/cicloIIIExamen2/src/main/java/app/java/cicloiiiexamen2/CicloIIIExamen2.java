package app.java.cicloiiiexamen2;

import clases.Empleado;
import java.util.Scanner;

public class CicloIIIExamen2 {

    public static void main(String[] args) {
        
        Empleado empleado = new Empleado();
        
        // INICIO DE INGRESO DE DATOS
        
        empleado.setDni(inputDni("DNI",8));
        empleado.setNombre(inputTexto("Nombre",3));
        empleado.setApellidoPaterno(inputTexto("Apellido Paterno",3));
        empleado.setApellidoMaterno(inputTexto("Apellido Materno",3));
        empleado.setSexo(inputSexo("Sexo"));
        empleado.setEstadoCivil(inputEstadoCivil("Estado Civil"));
        empleado.setNumeroHijos(inputHijos("Numero de Hijos",0));
        empleado.setSueldoBase(inputSueldo("Sueldo Base",1));
        
        // FIN DE INGRESO DE DATOS
        
        
        System.out.println(" Su Correo asignado es: " + empleado.getEmail());
        System.out.println(" Sueldo Bruto: " + empleado.getSueldoBruto());
        
    }
    
    public static String inputTexto(String dato,int minCaracteres){
        int i = 0;
        String texto = "";
        Scanner entrada = new Scanner(System.in);    
        
        while (i < minCaracteres){
            System.out.println("Ingrese su " + dato);
            texto = entrada.next();
            i = texto.length();
            if (i < minCaracteres){
                errorMensaje(dato);
            }            
        }
        return texto;
    }
    public static String inputDni(String dato,int minCaracteres){
        int i = 0;
        String texto = "";
        Scanner entrada = new Scanner(System.in);    
        
        while (i != minCaracteres){
            System.out.println("Ingrese su " + dato);
            texto = entrada.next();
            i = texto.length();
            if (minCaracteres != i){
                errorMensaje(dato);
            }
            
        }
        return texto;
    }
    public static String inputEstadoCivil(String dato){
        String valor = "";
        Scanner entrada = new Scanner(System.in);    
               
        while (!valor.equals("S") && !valor.equals("C") && !valor.equals("V") && !valor.equals("D")){
            System.out.println("Ingrese su " + dato);
            valor = entrada.next();
            valor = valor.toUpperCase();  
        }
        
        return valor;
    }
    public static String inputSexo(String dato){
        String valor;
        Scanner entrada = new Scanner(System.in);    
        System.out.println("Ingrese su " + dato);
        valor = entrada.next();
        valor = valor.toUpperCase();
        if (!valor.equals("M") && !valor.equals("F")){
            
            valor = "M";
        }
        System.out.println("Ingrese su " + valor);
        return valor;
    }
    public static double inputSueldo(String dato,int minCaracteres){
        double i = 0;
        double numero = 0;
        Scanner entrada = new Scanner(System.in);    
        
        do{
            System.out.println("Ingrese su " + dato);
            numero = entrada.nextInt();
            i = numero;
            if (i < minCaracteres){
                errorMensaje(dato);
            }
            
        }while (i < minCaracteres);
        return numero;
    }
    public static int inputHijos(String dato,int minCaracteres){
        int i = 0;
        int numero = 0;
        Scanner entrada = new Scanner(System.in);    
        
        do{
            System.out.println("Ingrese su " + dato);
            numero = entrada.nextInt();
            i = numero;
            if (i < minCaracteres){
                errorMensaje(dato);
            }
            
        }while (i < minCaracteres);
        return numero;
    }
    public static void errorMensaje(String dato){
        System.out.println("Error: " + dato + " no es valido por favor verifique nuevamente");
    }
}
