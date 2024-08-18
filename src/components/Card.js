import React, { useState } from 'react';
import axios from 'axios';

const Card = ({ img, title, season, day, date, id, category, onUpdate }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [editedTitle, setEditedTitle] = useState(title);
    const [editedSeason, setEditedSeason] = useState(season);
    const [editedDay, setEditedDay] = useState(day);
    const [editedDate, setEditedDate] = useState(date);
    const [editedCategory, setEditedCategory] = useState(category);

    const handleEdit = () => {
        setIsEditing(true);
    };

    const handleSave = () => {
        setIsEditing(false);
        axios.put(`http://127.0.0.1:5004/update/${id}`, {
            title: editedTitle,
            season: editedSeason,
            day: editedDay,
            date: editedDate,
            category: editedCategory
        })
            .then(response => {
                console.log('Item updated:', response.data);
                // Notify parent component about the update
                if (onUpdate) onUpdate(response.data);
            })
            .catch(error => console.error('Error updating item:', error));
    };

    return (
        <section className="card">
            <img src={img} alt={title} className="card-img" />
            <div className="card-details">
                {isEditing ? (
                    <>
                        <input
                            type="text"
                            className="card-title"
                            value={editedTitle}
                            onChange={(e) => setEditedTitle(e.target.value)}
                        />
                        <input
                            type="text"
                            className="card-season"
                            value={editedSeason}
                            onChange={(e) => setEditedSeason(e.target.value)}
                        />
                        <input
                            type="text"
                            className="card-day"
                            value={editedDay}
                            onChange={(e) => setEditedDay(e.target.value)}
                        />
                        <input
                            type="text"
                            className="card-date"
                            value={editedDate}
                            onChange={(e) => setEditedDate(e.target.value)}
                        />

                        <input
                            type="text"
                            className="card-category"
                            value={editedCategory}
                            onChange={(e) => setEditedCategory(e.target.value)}
                        />
                        <button onClick={handleSave}>Save</button>
                    </>
                ) : (
                    <>
                        <h3 className="card-title">{editedTitle}</h3>
                        <p className="card-season">{editedSeason}</p>
                        <p className="card-day">{editedDay}</p>
                        <p className="card-date">{editedDate}</p>

                        <button onClick={handleEdit}>Edit</button>
                    </>
                )}
            </div>
        </section>
    );
};

export default Card;
