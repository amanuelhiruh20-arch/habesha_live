import 'package:flutter/material.dart';

void main() {
  runApp(const HabeshaLiveApp());
}

class HabeshaLiveApp extends StatelessWidget {
  const HabeshaLiveApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Habesha Live',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('HABESHA LIVE (v2.4.0)'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Welcome to Habesha Live!\nA secure, modern social streaming infrastructure for Ethiopians and the global Habesha community.',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, height: 1.5),
            ),
            const SizedBox(height: 40),
            ElevatedButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const AboutScreen()),
                );
              },
              style: ElevatedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 16),
              ),
              child: const Text('About App & Info', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
            ),
          ],
        ),
      ),
    );
  }
}

class AboutScreen extends StatelessWidget {
  const AboutScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('About Habesha Live'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: ListView(
          children: const [
            Text(
              '👑 Habesha Live Platform Overview',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.blue),
            ),
            SizedBox(height: 15),
            Text(
              '• Overview & Reliability:\n'
              '  Built with advanced modern Flutter technology, Habesha Live provides a highly secure, reliable, and optimized infrastructure for real-time video streaming, interactive broadcasting, and community networking.\n\n'
              '• Version & Architecture:\n'
              '  - Version: v2.4.0 (Stable Production)\n'
              '  - Architecture: Modular, Low-Latency Stream Pipelines with Material 3 UI.\n\n'
              '• Leadership & Ownership:\n'
              '  - Founder & Lead Developer: Amanuel Kadire\n'
              '  - Head of Operations: Amanuel Kadire\n\n'
              '• Official Location / Address:\n'
              '  Addis Ababa, 4 Killo, Ethiopia\n\n'
              '📞 Contact & Support Credentials:\n'
              '• Phone Number: 0908718376\n'
              '• Telegram: @habesha live\n'
              '• Email: amanuelkadire712@gmail.com',
              style: TextStyle(fontSize: 15, height: 1.6),
            ),
          ],
        ),
      ),
    );
  }
}