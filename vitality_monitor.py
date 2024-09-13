import psutil
from jinja2 import Template
import os
import datetime

# Function to check system health
def system_health_check():
    health_data = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return health_data

# Function to generate HTML report
def generate_html_report(health_data):
    template = Template("""
    <html>
    <head>
        <title>System Health Report</title>
    </head>
    <body>
        <h1>System Vitality Report</h1>
        <p><strong>Report generated at:</strong> {{ health_data.timestamp }}</p>
        <p><strong>CPU Usage:</strong> {{ health_data.cpu_percent }}%</p>
        <p><strong>Memory Usage:</strong> {{ health_data.memory_percent }}%</p>
        <p><strong>Disk Usage:</strong> {{ health_data.disk_percent }}%</p>
    </body>
    </html>
    """)
    
    report = template.render(health_data=health_data)
    with open("system_health_report.html", "w") as file:
        file.write(report)

if __name__ == "__main__":
    health_data = system_health_check()
    print(f"CPU Usage: {health_data['cpu_percent']}%")
    print(f"Memory Usage: {health_data['memory_percent']}%")
    print(f"Disk Usage: {health_data['disk_percent']}%")
    
    # Generate HTML report
    generate_html_report(health_data)
    print("System health report generated: system_health_report.html")
