import { useEffect } from 'react';
import Cookies from 'js-cookie';
import axios from 'axios';

import {SESSION_COOKIE, SERVER_ADDRESS} from "./constants";

export default function App() {
  const cookieValue = Cookies.get(SESSION_COOKIE);
    useEffect(() => {
        if (cookieValue == null) {
            axios.post(`${SERVER_ADDRESS}/sign_up`, null, { withCredentials: true });
        }
    }, [cookieValue]);

    return (
        <main>
            <h1>Avalon</h1>
        </main>
    );
}
