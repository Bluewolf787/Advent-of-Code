import 'dart:async';
import 'dart:io';
import 'dart:convert';

void main() async {
  File file = File('input.txt');
  Stream<String> lines =
      file.openRead().transform(utf8.decoder).transform(LineSplitter());

  List list = [];

  try {
    int elfCount = 0;
    await for (var line in lines) {
      if (line.isEmpty) {
        list.add(elfCount);
        elfCount = 0;
      } else
        elfCount += int.parse(line);
    }
  } catch (e) {
    print('Error $e');
  }

  list.sort();
  print(list.last);
  print(list
      .getRange(list.length - 3, list.length)
      .reduce((value, element) => value + element));
}
