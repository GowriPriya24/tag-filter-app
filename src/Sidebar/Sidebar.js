import Category from "./Category/Category";
import Playlist from "./Playlist/Playlist";
import Day from "./Day/Day";

import "./Sidebar.css";

const Sidebar = ({ handleChange, handleDayChange, categories, addCategory, handlePlaylistChange }) => {
    return (
        <>
            <section className="sidebar">
                <div className="logo-container">
                    <h1>Welcome!</h1>
                </div>
                <Category
                    handleChange={handleChange}
                    categories={categories}
                    addCategory={addCategory}
                />
                <Playlist handlePlaylistChange={handlePlaylistChange} />
                <Day handleDayChange={handleDayChange} />
            </section>
        </>
    );
};

export default Sidebar;
