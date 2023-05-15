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
+++ 
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

+  TEST_ENV3: test-test3

+

+jobs:

+  test:

+    runs-on: ubuntu-latest

+

+    steps:

+      - name: Say Hello

+        run: echo "Hello, World!"
name: Test Workflow 1



on:

  push:

    branches:

      - main



env:

  TEST_ENV1: test-test1

  TEST_ENV2: test-test2

  TEST_ENV3: test-test3

  TEST_ENV4: test-test4

  TEST_ENV5: test-test5



jobs:

  test:

    runs-on: ubuntu-latest



    steps:

      - name: Say Hello

        run: echo "Hello, World!"
+++ 
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

+  TEST_ENV3: test-test3

+  TEST_ENV4: test-test4

+  TEST_ENV5: test-test5

+  TEST_ENV6: test-test6

+

+jobs:

+  test:

+    runs-on: ubuntu-latest

+

+    steps:

+      - name: Say Hello

+        run: echo "Hello, World!"
+++ +  push:

+    branches:

+      - main

+  TEST_ENV1: test-test1

+  TEST_ENV2: test-test2

+  TEST_ENV3: test-test3

+  TEST_ENV4: test-test4

+  TEST_ENV5: test-test5

+  TEST_ENV6: test-test6

+  TEST_ENV7: test-test7

+  TEST_ENV8: test-test8

+  test:

+    runs-on: ubuntu-latest

+    steps:

+      - name: Say Hello

+        run: echo "Hello, World!"
