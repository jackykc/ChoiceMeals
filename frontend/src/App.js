import React, { Component } from 'react'

// apollo imports
import ApolloClient from 'apollo-client';
import { createHttpLink, HttpLink } from 'apollo-link-http';
import { setContext } from 'apollo-link-context';
import { InMemoryCache } from 'apollo-cache-inmemory';
import { ApolloProvider } from 'react-apollo';
import { ApolloLink } from 'apollo-link';

import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom'
import CreateView from './views/CreateView'
import DetailView from './views/DetailView'
import ListView from './views/ListView'
import LoginView from './views/LoginView'
import LogoutView from './views/LogoutView'

// for graphql

const httpLink = createHttpLink({
    uri: 'http://127.0.0.1:8000/gql',
    credentials: 'same-origin'
});

const token = localStorage.getItem('token');

const middlewareLink = new ApolloLink((operation, forward) => {
  operation.setContext({
    headers: {
      authorization: `JWT ${token}` || null
    }
  });
  return forward(operation)
})

// const middlewareLink = setContext(() => ({
//     headers: {
//         authorization: `JWT ${token}` || null,
//     }

// }));

const link = middlewareLink.concat(httpLink);

const client = new ApolloClient({
    link,
    cache: new InMemoryCache().restore(window.__APOLLO_STATE__),
  });

class App extends Component {
    render() {
        console.log(middlewareLink.operation);
        return (
            <ApolloProvider client={client}>
                <Router>
                    <div>
                        <ul>
                            <li><Link to="/">Home</Link></li>
                            <li><Link to="/ingredient/create/">Create Message</Link></li>
                            <li><Link to="/login/">Login</Link></li>
                            <li><Link to="/logout/">Logout</Link></li>
                        </ul>
                        <Route exact path="/" component={ListView} />
                        <Route exact path="/login/" component={LoginView} />
                        <Route exact path="/logout/" component={LogoutView} />
                        <Switch>
                            <Route path="/ingredient/create/" component={CreateView} />
                            <Route path="/ingredient/:id/" component={DetailView} />
                        </Switch>
                    </div>
                </Router>
            </ApolloProvider>
        )
    }
}

export default App