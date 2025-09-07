export default async function handler(req, res) {
  const { type, id, name } = req.query;

  const API_BASE = 'https://api.clashofclans.com/v1';
  const TOKEN = process.env.API_TOKEN;

  if (!TOKEN) {
    return res.status(500).json({ error: "API token not configured" });
  }

  const headers = {
    Accept: 'application/json',
    Authorization: `Bearer ${TOKEN}`,
  };

  try {
    let url = '';
    switch (type) {
      case 'user':
        if (!id) {
          return res.status(400).json({ error: "Missing user id" });
        }
        url = `${API_BASE}/players/${encodeURIComponent(id)}`;
        break;

      case 'searchClans':
        if (!name) {
          return res.status(400).json({ error: "Missing clan name" });
        }
        url = `${API_BASE}/clans?name=${encodeURIComponent(name)}`;
        break;

      case 'goldpass':
        url = `${API_BASE}/goldpass/seasons/current`;
        break;

      default:
        return res.status(400).json({ error: "Invalid or missing 'type' query parameter" });
    }

    const response = await fetch(url, { headers });

    if (!response.ok) {
      const errorJson = await response.json();
      return res.status(response.status).json({ error: errorJson.reason || "API error" });
    }

    const data = await response.json();
    return res.status(200).json(data);
  } catch (err) {
    console.error('Fetch error:', err);
    return res.status(500).json({ error: 'Server error' });
  }
}
