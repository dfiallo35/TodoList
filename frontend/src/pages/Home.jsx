import { useEffect, useState } from 'react';
import api from '../api';


function Home() {
    const [home, setHome] = useState('');

    useEffect(() => {
        getHome();
    }, [])

    const getHome = () => {
        api
            .get('/api/')
            .then((res) => setHome(res.data.message))
            .catch((err) => alert(err));
    }

    return (
        <div>
            <h1>Home</h1>
            <p>{home}</p>
        </div>
    )
}

export default Home;