<div class="section-header">
  <h3 class="mb-4">Monthly Statistics</h3>
  <canvas id="monthlyChart"></canvas>
</div>
function exportMonthlyStats() {
  // Generate CSV data (you'll need to construct this based on your data)
  const csvData = "Month,Total Visits,Unique Visitors,Total Page Views,Total Sales\n" +
                  "January,1000,800,5000,200\n" +
                  // Add more data rows

  // Create a download link for the CSV file
  const blob = new Blob([csvData], { type: 'text/csv' });
  const url = window.URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'monthly_statistics.csv';
  link.click();
}
function generateReport() {
  // Construct report content (you'll need to customize this based on your data)
  const reportContent = `
    <h1>Monthly Report</h1>
    <p>Report generated on: ${new Date().toLocaleDateString()}</p>
    <h2>Monthly Statistics</h2>
    <ul>
      <li>Total Visits: 1000</li>
      <li>Unique Visitors: 800</li>
      <li>Total Page Views: 5000</li>
      <li>Total Sales: 200</li>
    </ul>
    <!-- Include more data -->
  `;

  // Create a new window with the report content
  const reportWindow = window.open('', '_blank');
  reportWindow.document.write(reportContent);
  reportWindow.document.close();
}