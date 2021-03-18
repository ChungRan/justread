import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';

import Book from './components/Book/Book';
import Navigation from './components/Navigation/Navigation';



const Router = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact={true} path="/" component={Book} />
        <Route path="/page1" component={Book} />
        <Route path="/page2" component={Navigation} />
        {/* Not Found */}
        <Route component={() => <Redirect to="/" />} />
      </Switch>
    </BrowserRouter>
  );
};

export default Router;