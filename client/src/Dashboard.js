import { useState } from "react";

function Dashboard(){
    const [items, setItems] = useState(["marlboro", "camel"]); 
    const [item, setItem] = useState("");

    const addItem = ()=> {
        setItems([...items, item]);
        setItem("");
    };

    const deleteItem = (name)=> {
        setItems(items.filter((item) => item !== name))
    };

    return(
        <>
            <input text="text" placeholder="enter location" onChange={ (event)=> setItem(event.target.value)} value={item} />
            <button onClick={addItem}>Add</button>
            <ul>
                {items.map((name) => (
                    <div>
                        <li key={name}>{name}</li>
                        <button onClick={() => deleteItem(name)}>Delete</button>
                    </div>
                ))}
            </ul>
        </>
    );
};

export default Dashboard;