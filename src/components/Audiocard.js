import React from 'react';

const AudioCard = ({ img, audioSrc, title }) => {
    return (
        <>
            <section className="audio-card">
                <img src={img} alt={title} className="audio-img" />
                <div className="audio-details">
                    <h3 className="audio-title">{title}</h3>
                    <audio controls className="audio-player">
                        <source src={audioSrc} type="audio/mpeg" />
                        Your browser does not support the audio element.
                    </audio>
                </div>
            </section>
        </>
    );
};

export default AudioCard;