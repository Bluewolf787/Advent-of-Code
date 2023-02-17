import 'dart:async';
import 'dart:convert';
import 'dart:io';

void main() async {
  File file = File('input.txt');
  Stream<String> lines =
      file.openRead().transform(utf8.decoder).transform(LineSplitter());

  List sections = [];

  try {
    List section = [];
    await for (var line in lines) {
      section.add(int.parse(line.split('-')[0]));
      section.add(int.parse(line.split(',')[0].split('-')[1]));
      section.add(int.parse(line.split(',')[1].split('-')[0]));
      section.add(int.parse(line.split('-')[2]));

      sections.add(List.from(section));
      section.clear();
    }
  } catch (error) {
    print('Error $error');
  }

  int count1 = 0;
  int count2 = 0;

  sections.forEach((s) {
    if ((s[0] >= s[2] && s[1] <= s[3]) || (s[2] >= s[0] && s[3] <= s[1]))
      count1++;
    if (!(s[1] < s[2] || s[3] < s[0])) count2++;
  });

  print(count1);
  print(count2);
}
