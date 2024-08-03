package clases;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
public class Empleado {
    private String dni;
    private String nombre;
    private String apellidoPaterno;
    private String apellidoMaterno;
    private String sexo;
    private String fechaNacimiento;
    private String estadoCivil;
    private double numeroHijos;
    private double sueldoBase;

    public String getDni() {
        return dni;
    }

    public void setDni(String dni) {
        this.dni = dni;
    }
    
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellidoPaterno() {
        return apellidoPaterno;
    }

    public void setApellidoPaterno(String apellidoPaterno) {
        this.apellidoPaterno = apellidoPaterno;
    }

    public String getApellidoMaterno() {
        return apellidoMaterno;
    }

    public void setApellidoMaterno(String apellidoMaterno) {
        this.apellidoMaterno = apellidoMaterno;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public String getFechaNacimiento() {
        return fechaNacimiento;
    }

    public void setFechaNacimiento(String fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }

    public String getEstadoCivil() {
        return estadoCivil;
    }

    public void setEstadoCivil(String estadoCivil) {
        this.estadoCivil = estadoCivil;
    }

    public double getNumeroHijos() {
        return numeroHijos;
    }

    public void setNumeroHijos(int numeroHijos) {
        this.numeroHijos = numeroHijos;
    }

    public double getSueldoBase() {
        return sueldoBase;
    }

    public void setSueldoBase(double sueldoBase) {
        this.sueldoBase = sueldoBase;
    }

    public double getSueldoBruto() {
        double sueldoBruto = sueldoBase;
        double hijos = numeroHijos;
//        
        if (this.estadoCivil.equals("C")){
            sueldoBruto = sueldoBruto + (sueldoBruto * 0.03);
        }
        if( 0 < hijos ){
            sueldoBruto = sueldoBruto + (sueldoBruto * 0.08);
        }
        return sueldoBruto;
    }
    public String getEmail(){
        String dato = nombre;
        char dato1 = dato.charAt(0);
        
        return apellidoPaterno.toLowerCase() + "." + apellidoMaterno.toLowerCase() + "." + dato1 + "@empresa.com";
    }

    
    public String getApellidos() {
        return this.apellidoPaterno + " " + apellidoMaterno;
    }
    
    public int getEdad(){
        DateTimeFormatter dtFormat = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        LocalDate fechaNac = LocalDate.parse(this.fechaNacimiento,dtFormat);
        LocalDate fechaActual = LocalDate.now();
        Period periodo = Period.between(fechaNac,fechaActual);
        return periodo.getYears();
    }
}
