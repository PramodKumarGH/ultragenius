import os
import csv

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Write members CSV
members_data = [
    ['name', 'surname', 'booking_count', 'date_joined'],
    ['Sophie', 'Davis', '1', '2024-01-02T12:10:11'],
    ['Emily', 'Johnson', '0', '2024-11-12T12:10:12'],
    ['Jessica', 'Rodriguez', '3', '2024-01-02T12:10:13'],
    ['Chloe', 'Brown', '2', '2024-01-02T12:10:14'],
    ['Amelia', 'Williams', '0', '2024-01-02T12:10:15'],
    ['Grace', 'Miller', '1', '2023-01-02T12:10:15'],
    ['Lily', 'Garcia', '1', '2023-01-02T12:10:15'],
    ['Ruby', 'Jones', '1', '2023-01-02T12:10:18'],
    ['Charlotte', 'Martinez', '1', '2023-01-02T12:10:19'],
    ['Evie', 'Smith', '2', '2023-01-02T12:10:20'],
    ['Matthew', 'Davis', '1', '2023-01-02T12:10:21'],
    ['Samuel', 'Garcia', '1', '2023-01-02T12:10:22'],
    ['Joshua', 'Smith', '1', '2023-01-02T12:10:23'],
    ['Jack', 'Rodriguez', '1', '2023-01-02T12:10:24'],
    ['James', 'Brown', '0', '2024-01-02T12:10:25'],
    ['Grace', 'Miller', '0', '2020-11-12T12:10:12'],
    ['Joseph', 'Miller', '0', '2020-11-12T12:10:12'],
    ['Jacob', 'Frye', '2', '2024-01-02T12:10:28'],
    ['Evie', 'Frye', '0', '2024-01-02T12:10:29'],
    ['Daniel', 'Johnson', '3', '2024-01-02T12:10:30'],
    ['Thomas', 'Williams', '0', '2024-01-02T12:10:31'],
    ['Luke', 'Wilson', '0', '2024-01-02T12:10:32'],
    ['Benjamin', 'Jones', '1', '2024-01-02T12:10:33'],
    ['Alexander', 'Martin', '1', '2022-01-02T12:10:34'],
    ['Harry', 'Moore', '2', '2022-01-02T12:10:35'],
    ['Faye', 'Hurst', '1', '2022-01-02T12:10:36'],
    ['Tiana', 'Silva', '0', '2022-01-02T12:10:37'],
    ['Aleena', 'Mahoney', '0', '2022-01-02T12:10:38'],
    ['Robert', 'Allen', '0', '2022-01-02T12:10:39'],
    ['Aaron', 'Mitchell', '0', '2022-01-02T12:10:40'],
    ['Sophie', 'Davis', '2', '2022-01-02T12:10:41'],
    ['Jacob', 'Green', '0', '2022-01-02T12:10:42'],
    ['Ben', 'Hill', '0', '2022-01-02T12:10:43'],
    ['Owen', 'Turner', '0', '2022-01-02T12:10:44'],
    ['Louis', 'Anderson', '0', '2024-01-02T12:10:45'],
    ['Liam', 'Jackson', '2', '2024-01-02T12:10:46'],
    ['Ryan', 'Hernandez', '0', '2024-01-02T12:10:47'],
    ['Adam', 'Thomas', '0', '2024-01-02T12:10:48'],
    ['Lewis', 'Thompson', '0', '2024-01-02T12:10:49'],
    ['Oliver', 'White', '0', '2024-01-02T12:10:50'],
    ['Callum', 'Taylor', '2', '2024-01-02T12:10:51'],
    ['William', 'Martinez', '0', '2024-01-02T12:10:52'],
    ['Lauren', 'Lang', '1', '2024-01-02T12:10:53'],
    ['Lena', 'Fernandez', '2', '2024-01-02T12:10:54'],
    ['Eden', 'Oneal', '3', '2024-01-02T12:10:55']
]

with open('data/members.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(members_data)

# Write inventory CSV
inventory_data = [
    ['title', 'description', 'remaining_count', 'expiration_date'],
    ['Bali', 'Suspendisse congue erat ac ex venenatis mattis. Sed finibus sodales nunc, nec maximus tellus aliquam id. Maecenas non volutpat nisl. Curabitur vestibulum ante non nibh faucibus, sit amet pulvinar turpis finibus', '5', '19/11/2030'],
    ['Madeira', 'Donec condimentum, risus non mollis sollicitudin, est neque sagittis metus, eget aliquam orci quam eget dui. Nam imperdiet, lorem quis lacinia imperdiet, augue libero tincidunt sem, eget pulvinar massa est non metus. Pellentesque et massa nibh.', '4', '20/11/2030'],
    ['Paris trip', 'Pellentesque non aliquam eros, quis posuere leo. Nullam sit amet tempor orci. Phasellus quam velit, aliquet nec nisl et, commodo rutrum lorem. Proin egestas nisl eget magna commodo sagittis. Integer egestas sodales mi eu maximus. Mauris et auctor felis, at dictum ipsum. Curabitur eros neque, commodo non mi congue, eleifend molestie quam. Cras feugiat, turpis sed ullamcorper vestibulum, enim lectus sagittis dui, ac semper nulla leo id arcu. Suspendisse auctor risus eu magna dapibus suscipit. Cras luctus dapibus turpis, vel ornare diam dignissim sed. Sed odio ipsum, placerat et mi eu, eleifend bibendum risus. Aliquam sed iaculis elit. Donec interdum egestas metus, quis sollicitudin nisi imperdiet id. Integer non ante eleifend mi viverra interdum eu nec nibh. Sed ac tortor lorem', '3', '21/11/2030'],
    ['F1 stage', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam in augue ut velit condimentum', '2', '22/11/2030'],
    ['Hot air balloon', 'Etiam molestie sem id luctus facilisis. Proin vestibulum, mauris vitae suscipit suscipit, metus enim faucibus metus, a bibendum nibh lorem id nisl', '1', '23/11/2021'],
    ['Route 66', 'Quisque at feugiat purus. Praesent feugiat eget sem quis tincidunt. Aliquam dui magna, auctor sit amet turpis nec, porttitor porta ero', '0', '24/11/2022'],
    ['Milano', 'Nunc laoreet purus eget tristique suscipit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos', '1', '25/11/2030'],
    ['Italy', 'Suspendisse potenti', '2', '26/11/2030'],
    ['Rome', 'Suspendisse dui felis, convallis in tortor vitae, lobortis molestie leo', '5', '27/11/2030'],
    ['France', 'Ut at euismod massa', '4', '28/11/2030'],
    ['Versailles', 'Sed tristique quam in elit bibendum tristique. Aliquam auctor, ante et pellentesque tristique, ipsum urna condimentum ante, vitae sodales ipsum augue ac massa.', '3', '29/11/2030'],
    ['London', 'Vestibulum in purus eu massa rutrum pretium ut non metus. Donec condimentum id elit eu convallis', '2', '30/11/2030'],
    ['London', 'Quisque ut eleifend turpis', '1', '01/12/2023'],
    ['Halifax', 'Nudus, turpis, Putridus, findere, Acerbus, crudus, Raptus, contemptio', '2', '02/12/2030'],
    ['England', 'Ut mauris orci, sodales ac pulvinar nec, posuere et metus.', '10', '03/12/2030']
]

with open('data/inventory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(inventory_data)

print("CSV files created successfully in the 'data' directory.")