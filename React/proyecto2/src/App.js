
import React, { useState } from 'react';

const FormComponent = () => {

  const [todo, setTodo] = useState({
      todoNombre: "",
      todoDescripcion: "",
      todoEstado: "pendiente",
      todoCheck: false,
  });


  const [error, setError] = useState(null);
  // Función para manejar el envío del formulario

  const handleSubmit = (e) => {
    e.preventDefault();

    const { todoNombre, todoDescripcion } = todo;

    // pequeña validación
    if (!todoNombre.trim() || !todoDescripcion.trim()) {
        console.log("campos vacíos");
        setError(true);
        return;
    } else {
        setError(false);
    }

    // Enviar todo a un array!
  };
  const handleChange = (e) => {
    const { name, value, checked, type } = e.target;

    setTodo((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
  }));

  const PintarError = () => (
    <div className="alert alert-danger">Todos los campos obligatorios</div>
  );


};

  return (
    <div className='container'>
      <h1 className='centrar mt-4'>Create Post</h1>
      {error && <PintarError />}
      <form onSubmit={handleSubmit} className='centrar'>
        <div>
          <label htmlFor="title">Id:</label>
          <input className='form-control' type="text"  id="id" value={id} onChange={(e) => setId(e.target.value)}  />
        </div>
        <div>
          <label htmlFor="title">User:</label>
          <input className='form-control' type="text"  id="userId" value={userId} onChange={(e) => setUserId(e.target.value)} />
        </div>
        <div>
          <label htmlFor="title">Title:</label>
          <input className='form-control' type="text"  id="title" value={title} onChange={(e) => setTitle(e.target.value)}  />
        </div>

        <div>
          <label htmlFor="body">Body:</label>
          <textarea className='form-control' id="body" value={body} onChange={(e) => setBody(e.target.value)}  ></textarea>
        </div>
        <div className="form-check">
          <input
              className="form-check-input"
              type="checkbox"
              id="flexCheckDefault"
              checked={todo.todoCheck}
              onChange={handleChange}
              name="todoCheck"
          />
          <label className="form-check-label" htmlFor="flexCheckDefault"> Dar prioridad </label>
      </div>
        <div>
          <label htmlFor="todoEstado">Estado:</label>
          <select className="form-control mb-2" name="todoEstado" id='todoEstado'>
            <option value="pendiente">Pendiente</option>
            <option value="completado">Completado</option>
          </select>
        </div>
        
        <br />
        <button type="submit" className='btn btn-success'>Submit</button>
      </form>
    </div>
  );

};


export default FormComponent;


//import React, { useState, useEffect } from 'react';

// const App = () => {
//   // Estado para almacenar los datos de la API
//   const [posts, setPosts] = useState([]);
//   // Estado para manejar errores
//   const [error, setError] = useState(null);
//   // Estado para manejar el estado de carga
//   const [loading, setLoading] = useState(true);

//   // useEffect para realizar la solicitud cuando el componente se monta
//   useEffect(() => {
//     const fetchPosts = async () => {
//       try {
//         const response = await fetch('https://jsonplaceholder.typicode.com/posts');
//         if (!response.ok) {
//           throw new Error('Network response was not ok');
//         }
//         const data = await response.json();
//         setPosts(data);
//       } catch (error) {
//         setError(error.message);
//       } finally {
//         setLoading(false);
//       }
//     };

//     fetchPosts();
//   }, []); // El array vacío indica que el efecto solo se ejecuta una vez al montar el componente

//   if (loading) {
//     return <div>Loading...</div>;
//   }

//   if (error) {
//     return <div>Error: {error}</div>;
//   }

//   return (
//     <div>
//       <h1>Posts</h1>
//       <ul>
//         {posts.map(post => (
//           <li key={post.id}>
//             <h2>{post.title}</h2>
//             <p>{post.body}</p>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default App;

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
