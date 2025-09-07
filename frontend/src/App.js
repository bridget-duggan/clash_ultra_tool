import React, { useState } from 'react';

function App() {
  const [tag, setTag] = useState('');
  const [clanData, setClanData] = useState(null);

  const fetchClanData = async () => {
    const res = await fetch(`https://your-vercel-project.vercel.app/api/clans?tag=${tag}`);
    const data = await res.json();
    setClanData(data);
  };

  return (
    <div>
      <h1>Clash of Clans Lookup</h1>
      <input value={tag} onChange={(e) => setTag(e.target.value)} placeholder="Enter clan tag" />
      <button onClick={fetchClanData}>Search</button>
      {clanData && (
        <pre>{JSON.stringify(clanData, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;

