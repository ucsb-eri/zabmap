<template>
<!-- Tree Root -->
<div class="hs-accordion-treeview-root" role="tree" aria-orientation="vertical">
  <!-- 1st Level Accordion Group -->
  <div class="hs-accordion-group" role="group" data-hs-accordion-always-open="">
    <!-- 1st Level Accordion -->
    <div class="hs-accordion active" role="treeitem" aria-expanded="true" id="hs-basic-usage-example-tree-heading-one">
      <!-- 1st Level Accordion Heading -->
      <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
        <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="true" aria-controls="hs-basic-usage-example-tree-collapse-one">
          <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M5 12h14"></path>
            <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
          </svg>
        </button>

        <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
          <div class="flex items-center gap-x-3">
            <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
            </svg>
            <div class="grow">
              <span class="text-sm text-gray-800 dark:text-neutral-200">
                assets
              </span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->

      <!-- 1st Level Collapse -->
      <div id="hs-basic-usage-example-tree-collapse-one" class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-heading-one">
        <!-- 2nd Level Accordion Group -->
        <div class="hs-accordion-group ps-7 relative before:absolute before:top-0 before:start-3 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700" role="group" data-hs-accordion-always-open="">
          <!-- 2nd Level Nested Accordion -->
          <div class="hs-accordion active" role="treeitem" aria-expanded="true" id="hs-basic-usage-example-tree-sub-heading-one">
            <!-- 2nd Level Accordion Heading -->
            <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
              <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="true" aria-controls="hs-basic-usage-example-tree-sub-collapse-one">
                <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
                </svg>
              </button>

              <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
                <div class="flex items-center gap-x-3">
                  <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
                  </svg>
                  <div class="grow">
                    <span class="text-sm text-gray-800 dark:text-neutral-200">
                      css
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->

            <!-- 2nd Level Collapse -->
            <div id="hs-basic-usage-example-tree-sub-collapse-one" class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-sub-heading-one">
              <!-- 3rd Level Accordion Group -->
              <div class="hs-accordion-group ps-7 relative before:absolute before:top-0 before:start-3 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700" role="group" data-hs-accordion-always-open="">
                <!-- 3rd Level Accordion -->
                <div class="hs-accordion active" role="treeitem" aria-expanded="true" id="hs-basic-usage-example-tree-sub-level-two-heading-one">
                  <!-- 3rd Level Accordion Heading -->
                  <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
                    <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="true" aria-controls="hs-basic-usage-example-tree-sub-level-two-collapse-one">
                      <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14"></path>
                        <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
                      </svg>
                    </button>

                    <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
                      <div class="flex items-center gap-x-3">
                        <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
                        </svg>
                        <div class="grow">
                          <span class="text-sm text-gray-800 dark:text-neutral-200">
                            main
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->

                  <!-- 3rd Level Collapse -->
                  <div id="hs-basic-usage-example-tree-sub-level-two-collapse-one" class="hs-accordion-content w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-sub-level-two-heading-one">
                    <div class="ms-3 ps-3 relative before:absolute before:top-0 before:start-0 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700">
                      <!-- 3rd Level Item -->
                      <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
                        <div class="flex items-center gap-x-3">
                          <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                            <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
                          </svg>
                          <div class="grow">
                            <span class="text-sm text-gray-800 dark:text-neutral-200">
                              main.css
                            </span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->

                      <!-- 3rd Level Item -->
                      <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
                        <div class="flex items-center gap-x-3">
                          <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                            <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
                          </svg>
                          <div class="grow">
                            <span class="text-sm text-gray-800 dark:text-neutral-200">
                              docs.css
                            </span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->

                      <!-- 3rd Level Item -->
                      <div class="px-2">
                        <span class="text-sm text-gray-800 dark:text-neutral-200">
                          README.txt
                        </span>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->

                <!-- 3rd Level Accordion -->
                <div class="hs-accordion" role="treeitem" aria-expanded="false" id="hs-basic-usage-example-tree-sub-level-two-heading-two">
                  <!-- 3rd Level Accordion Heading -->
                  <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
                    <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="false" aria-controls="hs-basic-usage-example-tree-sub-level-two-collapse-two">
                      <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M5 12h14"></path>
                        <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
                      </svg>
                    </button>

                    <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
                      <div class="flex items-center gap-x-3">
                        <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                          <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
                        </svg>
                        <div class="grow">
                          <span class="text-sm text-gray-800 dark:text-neutral-200">
                            tailwind
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <!-- End 3rd Level Accordion Heading -->

                  <!-- 3rd Level Collapse -->
                  <div id="hs-basic-usage-example-tree-sub-level-two-collapse-two" class="hs-accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-sub-level-two-heading-two">
                    <div class="ms-3 ps-3 relative before:absolute before:top-0 before:start-0 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700">
                      <!-- 3rd Level Item -->
                      <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
                        <div class="flex items-center gap-x-3">
                          <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                            <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
                          </svg>
                          <div class="grow">
                            <span class="text-sm text-gray-800 dark:text-neutral-200">
                              input.css
                            </span>
                          </div>
                        </div>
                      </div>
                      <!-- End 3rd Level Item -->
                    </div>
                  </div>
                  <!-- End 3rd Level Collapse -->
                </div>
                <!-- End 3rd Level Accordion -->

                <!-- 3rd Level Heading -->
                <div class="py-0.5 px-1.5" role="treeitem">
                  <span class="text-sm text-gray-800 dark:text-neutral-200">
                    .gitignore
                  </span>
                </div>
                <!-- End 3rd Level Heading -->
              </div>
              <!-- End 3rd Level Accordion Group -->
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->

          <!-- 2nd Level Nested Accordion -->
          <div class="hs-accordion" role="treeitem" aria-expanded="false" id="hs-basic-usage-example-tree-sub-heading-two">
            <!-- 2nd Level Accordion Heading -->
            <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
              <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="false" aria-controls="hs-basic-usage-example-tree-sub-collapse-two">
                <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
                </svg>
              </button>

              <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
                <div class="flex items-center gap-x-3">
                  <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
                  </svg>
                  <div class="grow">
                    <span class="text-sm text-gray-800 dark:text-neutral-200">
                      img
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->

            <!-- 2nd Level Collapse -->
            <div id="hs-basic-usage-example-tree-sub-collapse-two" class="hs-accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-sub-heading-two">
              <div class="ms-3 ps-3 relative before:absolute before:top-0 before:start-0 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700">
                <!-- 2nd Level Item -->
                <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
                  <div class="flex items-center gap-x-3">
                    <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                      <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
                      <circle cx="10" cy="12" r="2"></circle>
                      <path d="m20 17-1.296-1.296a2.41 2.41 0 0 0-3.408 0L9 22"></path>
                    </svg>
                    <div class="grow">
                      <span class="text-sm text-gray-800 dark:text-neutral-200">
                        hero.jpg
                      </span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->

                <!-- 2nd Level Item -->
                <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
                  <div class="flex items-center gap-x-3">
                    <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                      <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
                      <circle cx="10" cy="12" r="2"></circle>
                      <path d="m20 17-1.296-1.296a2.41 2.41 0 0 0-3.408 0L9 22"></path>
                    </svg>
                    <div class="grow">
                      <span class="text-sm text-gray-800 dark:text-neutral-200">
                        tailwind.png
                      </span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->

                <!-- 2nd Level Item -->
                <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
                  <div class="flex items-center gap-x-3">
                    <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                      <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
                      <circle cx="10" cy="12" r="2"></circle>
                      <path d="m20 17-1.296-1.296a2.41 2.41 0 0 0-3.408 0L9 22"></path>
                    </svg>
                    <div class="grow">
                      <span class="text-sm text-gray-800 dark:text-neutral-200">
                        untitled.png
                      </span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->

          <!-- 2nd Level Nested Accordion -->
          <div class="hs-accordion" role="treeitem" aria-expanded="false" id="hs-basic-usage-example-tree-sub-heading-three">
            <!-- 2nd Level Accordion Heading -->
            <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
              <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="false" aria-controls="hs-basic-usage-example-tree-sub-collapse-three">
                <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M5 12h14"></path>
                  <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
                </svg>
              </button>

              <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
                <div class="flex items-center gap-x-3">
                  <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
                  </svg>
                  <div class="grow">
                    <span class="text-sm text-gray-800 dark:text-neutral-200">
                      js
                    </span>
                  </div>
                </div>
              </div>
            </div>
            <!-- End 2nd Level Accordion Heading -->

            <!-- 2nd Level Collapse -->
            <div id="hs-basic-usage-example-tree-sub-collapse-three" class="hs-accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-sub-heading-three">
              <div class="ms-3 ps-3 relative before:absolute before:top-0 before:start-0 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700">
                <!-- 2nd Level Item -->
                <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
                  <div class="flex items-center gap-x-3">
                    <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                      <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
                      <circle cx="10" cy="12" r="2"></circle>
                      <path d="m20 17-1.296-1.296a2.41 2.41 0 0 0-3.408 0L9 22"></path>
                    </svg>
                    <div class="grow">
                      <span class="text-sm text-gray-800 dark:text-neutral-200">
                        preline.jpg
                      </span>
                    </div>
                  </div>
                </div>
                <!-- End 2nd Level Item -->
              </div>
            </div>
            <!-- End 2nd Level Collapse -->
          </div>
          <!-- End 2nd Level Nested Accordion -->
        </div>
        <!-- 2nd Level Accordion Group -->
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->

    <!-- 1st Level Accordion -->
    <div class="hs-accordion" role="treeitem" aria-expanded="false" id="hs-basic-usage-example-tree-heading-two">
      <!-- 1st Level Accordion Heading -->
      <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
        <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="false" aria-controls="hs-basic-usage-example-tree-collapse-two">
          <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M5 12h14"></path>
            <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
          </svg>
        </button>

        <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
          <div class="flex items-center gap-x-3">
            <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
            </svg>
            <div class="grow">
              <span class="text-sm text-gray-800 dark:text-neutral-200">
                scripts
              </span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->

      <!-- 1st Level Collapse -->
      <div id="hs-basic-usage-example-tree-collapse-two" class="hs-accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-heading-two">
        <div class="ms-3 ps-3 relative before:absolute before:top-0 before:start-0 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700">
          <!-- 1st Level Item -->
          <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
            <div class="flex items-center gap-x-3">
              <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
              </svg>
              <div class="grow">
                <span class="text-sm text-gray-800 dark:text-neutral-200">
                  preline.js
                </span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->

          <!-- 1st Level Item -->
          <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
            <div class="flex items-center gap-x-3">
              <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
              </svg>
              <div class="grow">
                <span class="text-sm text-gray-800 dark:text-neutral-200">
                  tailwind.js
                </span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->

          <!-- 1st Level Item -->
          <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
            <div class="flex items-center gap-x-3">
              <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
              </svg>
              <div class="grow">
                <span class="text-sm text-gray-800 dark:text-neutral-200">
                  www.js
                </span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->

    <!-- 1st Level Accordion -->
    <div class="hs-accordion" role="treeitem" aria-expanded="false" id="hs-basic-usage-example-tree-heading-three">
      <!-- 1st Level Accordion Heading -->
      <div class="hs-accordion-heading py-0.5 flex items-center gap-x-0.5 w-full">
        <button class="hs-accordion-toggle size-6 flex justify-center items-center hover:bg-gray-100 rounded-md focus:outline-hidden focus:bg-gray-100 disabled:opacity-50 disabled:pointer-events-none dark:hover:bg-neutral-700 dark:focus:bg-neutral-700" aria-expanded="false" aria-controls="hs-basic-usage-example-tree-collapse-three">
          <svg class="size-4 text-gray-800 dark:text-neutral-200" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M5 12h14"></path>
            <path class="hs-accordion-active:hidden block" d="M12 5v14"></path>
          </svg>
        </button>

        <div class="grow hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-1.5 rounded-md cursor-pointer">
          <div class="flex items-center gap-x-3">
            <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"></path>
            </svg>
            <div class="grow">
              <span class="text-sm text-gray-800 dark:text-neutral-200">
                templates
              </span>
            </div>
          </div>
        </div>
      </div>
      <!-- End 1st Level Accordion Heading -->

      <!-- 1st Level Collapse -->
      <div id="hs-basic-usage-example-tree-collapse-three" class="hs-accordion-content hidden w-full overflow-hidden transition-[height] duration-300" role="group" aria-labelledby="hs-basic-usage-example-tree-heading-three">
        <div class="ms-3 ps-3 relative before:absolute before:top-0 before:start-0 before:w-0.5 before:-ms-px before:h-full before:bg-gray-100 dark:before:bg-neutral-700">
          <!-- 1st Level Item -->
          <div class="hs-accordion-selectable hs-accordion-selected:bg-gray-100 dark:hs-accordion-selected:bg-neutral-700 px-2 rounded-md cursor-pointer" role="treeitem">
            <div class="flex items-center gap-x-3">
              <svg class="shrink-0 size-4 text-gray-500 dark:text-neutral-500" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path>
                <path d="M14 2v4a2 2 0 0 0 2 2h4"></path>
              </svg>
              <div class="grow">
                <span class="text-sm text-gray-800 dark:text-neutral-200">
                  index.html
                </span>
              </div>
            </div>
          </div>
          <!-- End 1st Level Item -->
        </div>
      </div>
      <!-- End 1st Level Collapse -->
    </div>
    <!-- End 1st Level Accordion -->
  </div>
  <!-- End 1st Level Accordion Group -->
</div>
</template>
<!-- End Tree Root -->
