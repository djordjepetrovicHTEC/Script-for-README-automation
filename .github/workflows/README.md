# Workflows

test
test
test
--- 
+++ 
@@ -0,0 +1,17 @@
+name: Test Workflow 1

+

+on:

+  push:

+    branches:

+      - main

+

+env:

+  TEST_ENV1: test-test1

+

+jobs:

+  test:

+    runs-on: ubuntu-latest

+

+    steps:

+      - name: Say Hello

+        run: echo "Hello, World!"
--- 
+++ 
@@ -0,0 +1,18 @@
+name: Test Workflow 1

+

+on:

+  push:

+    branches:

+      - main

+

+env:

+  TEST_ENV1: test-test1

+  TEST_ENV2: test-test2

+

+jobs:

+  test:

+    runs-on: ubuntu-latest

+

+    steps:

+      - name: Say Hello

+        run: echo "Hello, World!"
