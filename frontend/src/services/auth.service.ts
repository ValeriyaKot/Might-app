import { UserManager, WebStorageStateStore, User } from 'oidc-client';

export default class AuthService {
    userManager: UserManager;

    constructor() {

        const settings: any = {
            userStore: new WebStorageStateStore({ store: window.localStorage }),
            authority: "https://wsa-118-61",
            client_id: "Employee-Recognition-Platform.Hub.Client",
            redirect_uri: 'https://localhost:44357/callback.html',
            automaticSilentRenew: true,
            silent_redirect_uri: 'https://localhost:44357/silent-renew.html',
            response_type: 'code',
            scope: "EMP.Hub.API openid",
            post_logout_redirect_uri: 'https://localhost:44357/',
            filterProtocolClaims: true,
        };

        this.userManager = new UserManager(settings);
    }

    getUser(): Promise<User | null> {
        return this.userManager.getUser();
    }

    login(): Promise<void> {
        return this.userManager.signinRedirect();
    }

    logout(): Promise<void> {
        return this.userManager.signoutRedirect();
    }

    getAccessToken(): Promise<string> {
        return this.userManager.getUser().then((data: any) => {
            return data.access_token;
        });
    }

}