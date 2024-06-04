import { useEffect, useState } from 'react';
import api from '../api';
import Note from '../components/Note';
import "../styles/Home.css";


function Home() {
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");

    useEffect(() => {
        getNotes();
    }, [])

    const getNotes = () => {
        api
            .get("/todos")
            .then((res) => res.data)
            .then((data) => {
                setNotes(data);
                console.log("get notes", data);
            })
            .catch((err) => alert(err));
    };

    const createNote = (e) => {
        e.preventDefault();
        api.post("/todos",  {title, content})
            .then((response) => {
                if (response.status !== 201) {
                    alert("Error!")
                }
                setTitle("");
                setContent("");
                getNotes();
            })
            .catch((error) => console.error(error));
    }
    
    return (
        <div>
            <h2>Create Note</h2>
            <form onSubmit={createNote}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    onSubmit={() => setTitle("")}
                />
                <label htmlFor="content">Content:</label>
                <br />
                <textarea
                    id="content"
                    name="content"
                    required
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    onSubmit={(e) => setContent("")}
                ></textarea>
                <br />
                <input type="submit" value="Submit"></input>
            </form>
            <div>
                <h2>Notes</h2>
                {notes.map((note) => <Note note={note} key={note.id}/>)}
            </div>
        </div>
    )
}

export default Home;