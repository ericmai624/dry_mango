import * as React from 'react';

import FlexLayout from './common/FlexLayout.react';

const { useEffect } = React;

function App() {
  useEffect(() => {
    fetch('/crawl', { method: 'POST' });
  }, []);
  return <FlexLayout align="center">Hello</FlexLayout>;
}

export default App;
