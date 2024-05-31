import { useState } from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';
import { ACCESS_TOKEN, REFRESH_TOKEN } from '../constants';
import '../styles/Form.css';


function Form({route, method}) {
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const name = method === 'login' ? 'Login' : 'Register';

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();

        try {
            const res = await api.post(route, { userName, password });
            if (method == 'login') {
                localStorage.setItem(ACCESS_TOKEN, res.data.accessToken);
                localStorage.setItem(REFRESH_TOKEN, res.data.refreshToken);
                navigate('/');
            }
            else {
                navigate('/login');
            }
        }
        catch (error) {
            alert(error);
        }
        finally {
            setLoading(false);
        }
    }

    return (
        <form onSubmit={handleSubmit} className='form-container'>
            <h1>{name}</h1>
            <input
                className='form-input'
                type='text'
                value={userName}
                onChange={(e) => setUserName(e.target.value)}
                placeholder='Username'
            />
            <input
                className='form-input'
                type='password'
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder='Password'
            />
            <button className='form-button' type='submit'>
                {name}
            </button>
        </form>
    )
}

export default Form;