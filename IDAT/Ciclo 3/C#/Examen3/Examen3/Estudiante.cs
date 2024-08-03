using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Examen3
{
    class Estudiante
    {
        private int _id;
        private string _nombre;
        private string _celular;
        private string _edad;
        private string _genero;
        private string _email;
        private string _fechaAdmision;
        private string _clase;

        public int Codigo
        {
            get
            {
                return _id;
            }
            set
            {
                _id = value;
            }
        }
        public string Nombre
        {
            get
            {
                return _nombre;
            }
            set
            {
                _nombre = value;
            }
        }
        public string Celular
        {
            get
            {
                return _celular;
            }
            set
            {
                _celular = value;
            }
        }
        public string Edad
        {
            get
            {
                return _edad;
            }
            set
            {
                _edad = value;
            }
        }
        public string Genero
        {
            get
            {
                return _genero;
            }
            set
            {
                _genero = value;
            }
        }
        public string Email
        {
            get
            {
                return _email;
            }
            set
            {
                _email = value;
            }
        }
        public string FechaAdmision
        {
            get
            {
                return _fechaAdmision;
            }
            set
            {
                _fechaAdmision = value;
            }
        }
        public string Clase
        {
            get
            {
                return _clase;
            }
            set
            {
                _clase = value;
            }
        }

        public Estudiante(int id, string nombre, string edad, string celular, string email, string genero, string clase, string fechaAdmision)
        {
            _id = id;
            _nombre = nombre;
            _celular = celular;
            _edad = edad;
            _genero = genero;
            _email = email;
            _fechaAdmision = fechaAdmision;
            _clase = clase;
        }

    }
}
