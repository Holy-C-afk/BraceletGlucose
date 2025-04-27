document.addEventListener('DOMContentLoaded', function() {
    // Initialize Chart
    const ctx = document.getElementById('glucoseChart').getContext('2d');
    let glucoseChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Glucose Level',
                data: [],
                borderColor: '#4CAF50',
                backgroundColor: 'rgba(76, 175, 80, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    mode: 'index',
                    intersect: false,
                    callbacks: {
                        label: function(context) {
                            return `Glucose: ${context.parsed.y} mg/dL`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });

    // Time Range Selector
    const timeRangeSelect = document.getElementById('timeRange');
    timeRangeSelect.addEventListener('change', function() {
        updateChartData(this.value);
    });

    // Settings Modal
    const settingsModal = new bootstrap.Modal(document.getElementById('settingsModal'));
    const settingsButton = document.getElementById('settingsButton');
    const saveSettingsButton = document.getElementById('saveSettings');

    settingsButton.addEventListener('click', function() {
        settingsModal.show();
    });

    saveSettingsButton.addEventListener('click', function() {
        const timeRange = document.getElementById('defaultTimeRange').value;
        const glucoseUnit = document.getElementById('glucoseUnit').value;
        const chartType = document.getElementById('chartType').value;

        // Save settings to localStorage
        localStorage.setItem('dashboardSettings', JSON.stringify({
            timeRange,
            glucoseUnit,
            chartType
        }));

        // Update chart
        updateChartData(timeRange);
        glucoseChart.config.type = chartType;
        glucoseChart.update();

        settingsModal.hide();
    });

    // Load saved settings
    function loadSettings() {
        const savedSettings = localStorage.getItem('dashboardSettings');
        if (savedSettings) {
            const settings = JSON.parse(savedSettings);
            document.getElementById('defaultTimeRange').value = settings.timeRange;
            document.getElementById('glucoseUnit').value = settings.glucoseUnit;
            document.getElementById('chartType').value = settings.chartType;
            timeRangeSelect.value = settings.timeRange;
            glucoseChart.config.type = settings.chartType;
            glucoseChart.update();
        }
    }

    // Update Chart Data
    function updateChartData(timeRange) {
        // This would typically fetch data from your backend
        // For now, we'll use sample data
        const now = new Date();
        const data = [];
        const labels = [];

        switch(timeRange) {
            case '24h':
                for (let i = 24; i >= 0; i--) {
                    const time = new Date(now - i * 60 * 60 * 1000);
                    labels.push(time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
                    data.push(Math.random() * 100 + 100); // Random glucose values between 100-200
                }
                break;
            case '7d':
                for (let i = 7; i >= 0; i--) {
                    const time = new Date(now - i * 24 * 60 * 60 * 1000);
                    labels.push(time.toLocaleDateString([], { weekday: 'short' }));
                    data.push(Math.random() * 100 + 100);
                }
                break;
            case '30d':
                for (let i = 30; i >= 0; i--) {
                    const time = new Date(now - i * 24 * 60 * 60 * 1000);
                    labels.push(time.toLocaleDateString([], { month: 'short', day: 'numeric' }));
                    data.push(Math.random() * 100 + 100);
                }
                break;
        }

        glucoseChart.data.labels = labels;
        glucoseChart.data.datasets[0].data = data;
        glucoseChart.update();
    }

    // Initialize
    loadSettings();
    updateChartData(timeRangeSelect.value);

    // Update Quick Stats
    function updateQuickStats() {
        // This would typically fetch data from your backend
        const latestGlucose = Math.round(Math.random() * 100 + 100);
        const todayInsulin = Math.round(Math.random() * 20 + 10);
        const avgGlucose = Math.round(Math.random() * 50 + 100);

        document.getElementById('latestGlucose').textContent = `${latestGlucose} mg/dL`;
        document.getElementById('todayInsulin').textContent = `${todayInsulin} units`;
        document.getElementById('avgGlucose').textContent = `${avgGlucose} mg/dL`;
    }

    updateQuickStats();
}); 