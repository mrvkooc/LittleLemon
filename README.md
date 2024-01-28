to run the server: pls consider the MySQL credentials (root  12345678)

static page with an image is: http://127.0.0.1:8000/restaurant/
                              http://localhost:8000/restaurant/booking/tables
                                    it will give you an authentication error
                                        to get access:
                                            register a user at http://127.0.0.1:8000/auth/users/
                                            use it to log in at http://127.0.0.1:8000/auth/token/login and get a token
                                            call again the endpoint http://localhost:8000/restaurant/booking/tables but in insomnia add an auth with bearer token <token> and prefix Token
