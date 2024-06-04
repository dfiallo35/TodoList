import React from "react";
import "../styles/Note.css";


function Note({ note }) {
    return (
        <div className="note-container">
            <p className="note-title">{note.title}</p>
            <p className="note-content">{note.content}</p>
        </div>
    )
}

export default Note;