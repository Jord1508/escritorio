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
    private String numeroHijos;
    private String sueldoBase;
    private String  sueldoBruto;

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

    public String getNumeroHijos() {
        return numeroHijos;
    }

    public void setNumeroHijos(String numeroHijos) {
        this.numeroHijos = numeroHijos;
    }

    public String getSueldoBase() {
        return sueldoBase;
    }

    public void setSueldoBase(String sueldoBase) {
        this.sueldoBase = sueldoBase;
    }

    public String getSueldoBruto() {
        return sueldoBruto;
    }

    public void setSueldoBruto(String sueldoBruto) {
        this.sueldoBruto = sueldoBruto;
    }
    
    public int getEdad(){
        DateTimeFormatter dtFormat = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        LocalDate fechaNac = LocalDate.parse(this.fechaNacimiento,dtFormat);
        LocalDate fechaActual = LocalDate.now();
        Period periodo = Period.between(fechaNac,fechaActual);
        return periodo.getYears();
    }
}
