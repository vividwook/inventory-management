import { useEffect, useState } from "react";
import axios from "axios";

export default function App() {
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    axios.get("/api/devices").then(res => setDevices(res.data));
  }, []);

  return (
    <main className="p-4">
      <h1>Inventory Management</h1>
      <table>
        <thead><tr><th>ID</th><th>Name</th><th>Location</th><th>Status</th></tr></thead>
        <tbody>
          {devices.map(d => (
            <tr key={d.id}><td>{d.id}</td><td>{d.name}</td><td>{d.location}</td><td>{d.status}</td></tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
