import csv


def export_to_csv(volumes, filename):
    # Export volumes to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Volume ID', 'Volume Name'])

        for volume in volumes:
            writer.writerow([volume.id, volume.display_name])
