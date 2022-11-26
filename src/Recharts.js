import { LineChart, Line } from 'recharts';
const data = [{name: 'Page A', uv: 400, pv: 2400, amt: 2400},
              {name: 'Page A', uv: 200, pv: 2800, amt: 4000},
              {name: 'Page A', uv: 200, pv: 2800, amt: 4000},
              {name: 'Page A', uv: 300, pv: 2800, amt: 4000}, ];

export const CustomLineChart = () => (
  <LineChart width={400} height={400} data={data}>
    <Line type="monotone" dataKey="uv" stroke="#8884d8" />
  </LineChart>
);
