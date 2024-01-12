import axios from "axios";
import AuthService from "../services/auth.service";

const baseDomain = "http://localhost:8000/api";
const baseURL = `${baseDomain}`;

let apiClient = axios.create({
    baseURL
});

const injectToken = async(config) => {
    let newConfig = config;
    let auth = new AuthService();
    const response = await auth.getAccessToken()
    newConfig.headers.authorization = `Bearer ${response}`;
    newConfig.headers.common["Content-Type"] = "multipart/form-data";
    return newConfig

};
apiClient.interceptors.request.use(injectToken);
export default apiClient;