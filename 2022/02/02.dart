import 'dart:async';
import 'dart:convert';
import 'dart:io';

void main() async {
  File file = File('input.txt');
  Stream<String> lines =
      file.openRead().transform(utf8.decoder).transform(LineSplitter());

  await for (var line in lines) {}
}
