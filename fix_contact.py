import glob

files = glob.glob('*.html')

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # 1. Remove the skew background element
    content = content.replace(
        '<div class="absolute top-0 right-0 w-1/2 h-full bg-white -skew-x-12 translate-x-32 opacity-100 z-0 hidden lg:block"></div>',
        ''
    )

    # 2. Make form wrapper more pronounced
    # old: class="bg-white p-8 md:p-12 rounded-3xl shadow-[0_20px_40px_-15px_rgba(0,0,0,0.05)] border border-gray-100 relative"
    # new: class="bg-white p-8 md:p-14 rounded-3xl shadow-2xl border-t-4 border-[#ae8f73] relative"
    content = content.replace(
        'class="bg-white p-8 md:p-12 rounded-3xl shadow-[0_20px_40px_-15px_rgba(0,0,0,0.05)] border border-gray-100 relative"',
        'class="bg-white p-8 md:p-12 rounded-3xl shadow-[0_20px_60px_-15px_rgba(0,0,0,0.1)] border-t-4 border-[#ae8f73] relative"'
    )

    # 3. Inputs definition
    # old: class="w-full px-5 py-4 bg-[#f9f8f6] border border-transparent text-[#242424] rounded-xl focus:ring-1 focus:ring-[#ae8f73] focus:border-[#ae8f73] transition-colors outline-none"
    # new: class="w-full px-5 py-4 bg-[#f9f8f6] border border-gray-200 text-[#242424] rounded-xl focus:ring-2 focus:ring-[#ae8f73]/20 focus:border-[#ae8f73] transition-colors outline-none"
    content = content.replace(
        'class="w-full px-5 py-4 bg-[#f9f8f6] border border-transparent text-[#242424] rounded-xl focus:ring-1 focus:ring-[#ae8f73] focus:border-[#ae8f73] transition-colors appearance-none outline-none"',
        'class="w-full px-5 py-4 bg-white border border-gray-300 text-[#242424] rounded-xl focus:ring-2 focus:ring-[#ae8f73]/20 focus:border-[#ae8f73] transition-colors appearance-none outline-none shadow-sm"'
    )
    content = content.replace(
        'class="w-full px-5 py-4 bg-[#f9f8f6] border border-transparent text-[#242424] rounded-xl focus:ring-1 focus:ring-[#ae8f73] focus:border-[#ae8f73] transition-colors outline-none"',
        'class="w-full px-5 py-4 bg-white border border-gray-300 text-[#242424] rounded-xl focus:ring-2 focus:ring-[#ae8f73]/20 focus:border-[#ae8f73] transition-colors outline-none shadow-sm"'
    )

    with open(file, 'w') as f:
        f.write(content)
        print(f"Updated {file}")

