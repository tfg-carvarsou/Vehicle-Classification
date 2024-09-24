import { expect, test } from '@playwright/test';
import path from 'path';

test.describe('Ejecución de inferencias', () => {
    test('Inferencia de detección de vehículos con YOLOv5s', async ({ page }) => {
        const baseUrl = 'http://localhost:5173/'
        await page.goto(baseUrl)

        // Select the model type, model series and image to upload
        await page.getByAltText('Detector icon').click()
        await page.getByAltText('YOLOv5s detector image').click()
        const imageToUpload = path.join(process.cwd(), '/src/assets/static/detector/carretera.jpg')
        await page.getByAltText('Dropzone').setInputFiles(imageToUpload)

        // Confirm the image upload by accepting the terms of service
        await page.getByRole('button', { name: 'Upload image'}).click()
        await expect(page.getByText('Confirm uploading this image')).toBeVisible();
        await page.waitForTimeout(1000)
        await page.getByRole('button', { name: 'Upload now'}).click()
        await expect(page.getByText('Image uploaded successfully')).toBeVisible();

        // Check the inference results
        await page.getByRole('button', { name: 'Check results'}).click()
        await page.waitForTimeout(1000)
        await expect(page.getByText('Inference Results')).toBeVisible();
    })

    test('Inferencia de detección de vehículos con YOLOv8s', async ({ page }) => {
        const baseUrl = 'http://localhost:5173/'
        await page.goto(baseUrl)

        // Select the model type, model series and image to upload
        await page.getByAltText('Detector icon').click()
        await page.getByAltText('YOLOv8s detector image').click()
        const imageToUpload = path.join(process.cwd(), '/src/assets/static/detector/carretera.jpg')
        await page.getByAltText('Dropzone').setInputFiles(imageToUpload)

        // Confirm the image upload by accepting the terms of service
        await page.getByRole('button', { name: 'Upload image'}).click()
        await expect(page.getByText('Confirm uploading this image')).toBeVisible();
        await page.waitForTimeout(1000)
        await page.getByRole('button', { name: 'Upload now'}).click()
        await expect(page.getByText('Image uploaded successfully')).toBeVisible();

        // Check the inference results
        await page.getByRole('button', { name: 'Check results'}).click()
        await page.waitForTimeout(1000)
        await expect(page.getByText('Inference Results')).toBeVisible();
    })

    test('Inferencia de clasificación de vehículos con EfficientNetB1', async ({ page }) => {
        const baseUrl = 'http://localhost:5173/'
        await page.goto(baseUrl)

        // Select the model type, model series and image to upload
        await page.getByAltText('Classifier icon').click()
        await page.getByAltText('EfficientNetB1 classifier image').click()
        const imageToUpload = path.join(process.cwd(), '/src/assets/static/classifier/ram.jpg')
        await page.getByAltText('Dropzone').setInputFiles(imageToUpload)

        // Confirm the image upload by accepting the terms of service
        await page.getByRole('button', { name: 'Upload image'}).click()
        await expect(page.getByText('Confirm uploading this image')).toBeVisible();
        await page.waitForTimeout(1000)
        await page.getByRole('button', { name: 'Upload now'}).click()
        await expect(page.getByText('Image uploaded successfully')).toBeVisible();

        // Check the inference results
        await page.getByRole('button', { name: 'Check results'}).click()
        await page.waitForTimeout(1000)
        await expect(page.getByText('Inference Results')).toBeVisible();
    })

    test('Inferencia de clasificación de vehículos con YOLOv8s-cls', async ({ page }) => {
        const baseUrl = 'http://localhost:5173/'
        await page.goto(baseUrl)

        // Select the model type, model series and image to upload
        await page.getByAltText('Classifier icon').click()
        await page.getByAltText('YOLOv8s-cls classifier image').click()
        const imageToUpload = path.join(process.cwd(), '/src/assets/static/classifier/ram.jpg')
        await page.getByAltText('Dropzone').setInputFiles(imageToUpload)

        // Confirm the image upload by accepting the terms of service
        await page.getByRole('button', { name: 'Upload image'}).click()
        await expect(page.getByText('Confirm uploading this image')).toBeVisible();
        await page.waitForTimeout(1000)
        await page.getByRole('button', { name: 'Upload now'}).click()
        await expect(page.getByText('Image uploaded successfully')).toBeVisible();

        // Check the inference results
        await page.getByRole('button', { name: 'Check results'}).click()
        await page.waitForTimeout(1000)
        await expect(page.getByText('Inference Results')).toBeVisible();
    })
})